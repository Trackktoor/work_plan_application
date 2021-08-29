from flask import Blueprint, render_template

work_plan = Blueprint('worak_plan_blueprint', __name__, template_folder='templates')

@work_plan.route('/all_work')
def all_posts():
    return render_template('work_plan/all_work.html')