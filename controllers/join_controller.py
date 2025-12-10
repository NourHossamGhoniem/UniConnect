# controllers/join_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from repositories.join_repository import JoinRequestRepository
from models.join_request import JoinRequest

# Blueprint for join request routes
join_bp = Blueprint('join', __name__, template_folder='../templates', url_prefix='/join')

repo = JoinRequestRepository()

@join_bp.route('/', methods=['GET'])
def index():
    """
    Show the join form.
    Optionally show the student's own requests when ?student=<id> is supplied.
    """
    student = request.args.get('student', '').strip()
    student_requests = repo.get_by_student(student) if student else []
    return render_template('join_requests.html', student=student, requests=student_requests)

@join_bp.route('/submit', methods=['POST'])
def submit():
    """Handle form submission from students to create a join request."""
    student = (request.form.get('student') or '').strip()
    club = (request.form.get('club') or '').strip()

    if not student or not club:
        flash('Please provide both Student and Club fields.', 'danger')
        return redirect(url_for('join.index'))

    jr = JoinRequest(student=student, club=club)
    repo.add(jr)
    flash('Your join request was submitted.', 'success')
    # Redirect back to the form and show user's requests
    return redirect(url_for('join.index', student=student))

@join_bp.route('/manage/<club_id>', methods=['GET'])
def manage(club_id):
    """
    Club leader view: list all join requests for a club.
    In a real app you'd verify the leader's identity; here we keep it simple.
    """
    requests = repo.get_by_club(club_id)
    return render_template('manage_requests.html', club_id=club_id, requests=requests)

@join_bp.route('/manage/<club_id>/update', methods=['POST'])
def update(club_id):
    """
    Handle approve/reject actions from the manage page.
    Expects form fields: request_id, action ('approve'|'reject')
    """
    request_id = request.form.get('request_id', '').strip()
    action = request.form.get('action', '').strip().lower()

    if action not in ('approve', 'reject'):
        flash('Invalid action.', 'danger')
        return redirect(url_for('join.manage', club_id=club_id))

    new_status = 'approved' if action == 'approve' else 'rejected'
    updated = repo.update_status(request_id, new_status)
    if updated:
        flash(f'Request updated: {new_status}.', 'success')
    else:
        flash('Request not found.', 'warning')

    return redirect(url_for('join.manage', club_id=club_id))