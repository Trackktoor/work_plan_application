import graphene
from graphene import ObjectType, String, Int, DateTime, List, Field, ID
from models import *

class WorkForQuery(ObjectType):
    title_work = String()
    work_plan_id = Int()
    date_start = DateTime()
    date_end = DateTime()
    work_id = ID()

class WorkPlanQuery(ObjectType):
    id = ID()
    title = String()
    version = Int()

class Query(ObjectType):
    all_works = List(WorkForQuery, work_plan_id=Int())
    create_work = Field(WorkForQuery, title_work=String(), date_start=DateTime(), date_end=DateTime(), work_plan_id=Int())
    all_versions_for_work_plan = List(WorkPlanQuery, work_plan_title=String())


    def resolve_all_works(self, info, work_plan_id):
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first()
        works = [WorkForQuery(title_work=w.title, work_plan_id=work_plan_id, date_start=w.date_start, date_end=w.date_end, work_id=w.id) for w in work_plan.works]

        return works

    def resolve_create_work(self, info, title_work, date_start, date_end, work_plan_id):
        work = Work(title=title_work, date_start=date_start, date_end=date_end)
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first_or_404() 
        new_version_work_plan = Work_plan(title=work_plan.title, version=work_plan.version+1)
        for w in [w for w in work_plan.works]:
            new_version_work_plan.works.append(w)
        new_version_work_plan.works.append(work)

        db.session.add(work)
        db.session.add(new_version_work_plan)
        db.session.commit()

        return {"data": "ok"}

    def resolve_all_versions_for_work_plan(self, info, work_plan_title):
        work_plans = Work_plan.query.filter(Work_plan.title == work_plan_title).all()
        return work_plans

shema = graphene.Schema(query=Query, auto_camelcase=False )

