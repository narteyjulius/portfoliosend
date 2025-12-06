class SkillsRouter:
    """
    Routes the Skill model to the skills_db database.
    """
    route_app_labels = {"skills"}  # app name

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "skills_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "skills_db"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "skills_db"
        return None
