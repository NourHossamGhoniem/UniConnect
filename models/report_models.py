
from models.user_models import users
from models.club_models import clubs
from models.office_models import offices
from models.join_request_models import join_requests

def get_reports_data():
    total_users = len(users)
    total_clubs = len(clubs)
    total_offices = len(offices)
    total_members = sum(len(c.get('club_committee', [])) + 1 for c in clubs)  # +1 لل leader
    total_join_requests = len(join_requests)

    return {
        "total_users": total_users,
        "total_clubs": total_clubs,
        "total_offices": total_offices,
        "total_members": total_members,
        "total_join_requests": total_join_requests
    }

# تقرير متقدم: أكثر الأندية نشاطًا
def most_active_clubs():
    # نشاط حسب عدد الانضمامات (join_requests)
    activity = {}
    for club in clubs:
        club_id = club['club_id']
        count = sum(1 for req in join_requests if req['club_id'] == club_id and req['status'] == 'Approved')
        activity[club['club_name']] = count
    # ترتيب تنازلي
    return sorted(activity.items(), key=lambda x: x[1], reverse=True)
