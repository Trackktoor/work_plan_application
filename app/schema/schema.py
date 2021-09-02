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
    delete_work = Field(WorkPlanQuery, id=ID(), work_plan_id=ID())
    change_work = Field(WorkPlanQuery, id=ID(), work_plan_id=ID(), change=String())

    def resolve_all_works(self, info, work_plan_id):
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first()
        works = [WorkForQuery(title_work=w.title, work_plan_id=work_plan_id, date_start=w.date_start, date_end=w.date_end, work_id=w.id) for w in work_plan.works]

        return works

    def resolve_create_work(self, info, title_work, date_start, date_end, work_plan_id):
        work = Work(title=title_work, date_start=date_start, date_end=date_end)
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first_or_404() 

        new_version_work_plan = Work_plan(title=work_plan.title[:-2]+" "+str(work_plan.version+1), version=work_plan.version+1, id=work_plan.id+1)
        for w in [w for w in work_plan.works]:
            new_version_work_plan.works.append(w)
        print(work)
        new_version_work_plan.works.append(work)

        db.session.add(work)
        db.session.add(new_version_work_plan)
        db.session.commit()

        return {"data": "ok"}

    def resolve_all_versions_for_work_plan(self, info, work_plan_id):
        work_plans = Work_plan.query.filter(Work_plan.id == work_plan_id).all()
        return work_plans

    def resolve_delete_work(self, info, id, work_plan_id):
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first()
        try:
            work = [work for work in work_plan.works if work.id == int(id)][0]
            print(work_plan.works)

            new_version_work_plan = Work_plan(title=work_plan.title[:-2]+" "+str(work_plan.version+1), version=work_plan.version+1, id=work_plan.id+1)

            for w in [w for w in work_plan.works]:
                new_version_work_plan.works.append(w)

            new_version_work_plan.works.remove(work) 

            db.session.add(work)
            db.session.add(new_version_work_plan)
            db.session.commit()

            return {"data": ["ok"]}
        except:
            return {"data": ["Err"]}

    def resolve_change_work(self, info, work_plan_id, id, change): # 'date_start: 2021-08-30 13:12:00'
        work_plan = Work_plan.query.filter(Work_plan.id == work_plan_id).first()
        work = [work for work in work_plan.works if work.id == int(id)][0]

        params_for_change_work = change.split(',')
        params_for_change_work = [par.split('=') for par in params_for_change_work]
        new_work = Work(title=work.title, date_start=work.date_start, date_end=work.date_end, id=work.id+1)
        for par in params_for_change_work:
            if par[0] == 'date_start':
                new_work.date_start = par[1]
            elif par[0] == 'title':
                new_work.title = par[1]
            elif par[0] == 'date_end':
                new_work.date_end = par[1]

    
        new_version_work_plan = Work_plan(title=work_plan.title[:-2]+" "+str(work_plan.version+1), version=work_plan.version+1, id=work_plan.id+1)
        for w in [w for w in work_plan.works]:
            if not w.id == work.id:
                new_version_work_plan.works.append(w)

        new_version_work_plan.works.append(new_work)

        for w in new_version_work_plan.works:
            print(w)
        
        db.session.add(new_work)
        db.session.add(new_version_work_plan)
        db.session.commit()
        
        return 'WorkPlanQuery'


        

shema = graphene.Schema(query=Query, auto_camelcase=False )

