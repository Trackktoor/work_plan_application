import graphene
from graphene import ObjectType, String, Int, DateTime, List
from models import *

class WorkForQuery(ObjectType):
    title_work = String()
    work_plan_id = Int()
    date_start = DateTime()
    date_end = DateTime()
    work_id = graphene.ID()

class Query(ObjectType):
    all_works = List(WorkForQuery, work_plan_id=Int())

    def resolve_all_works(self, info, work_plan_id):
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first()
        works = [WorkForQuery(title_work=w.title, work_plan_id=work_plan_id, date_start=w.date_start, date_end=w.date_end, work_id=w.id) for w in work_plan.works]

        return works

shema = graphene.Schema(query=Query, auto_camelcase=False )

