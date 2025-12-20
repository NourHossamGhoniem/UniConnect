from flask import Blueprint, render_template
from models.report_models import get_reports_data, most_active_clubs

reports_bp = Blueprint('reports', __name__, url_prefix='/reports')

@reports_bp.route('/analytics')
def analytics():
    data = get_reports_data()
    active_clubs = most_active_clubs()
    return render_template('analytics.html', data=data, active_clubs=active_clubs)
