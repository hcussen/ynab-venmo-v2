From now on, whenever you need to make schema changes:

1. Update your models in `app/models.py`
2. Run `alembic revision --autogenerate -m "Description of change"`
3. Review the generated migration in `migrations/versions/`
4. Apply with `alembic upgrade head`
5. Commit all changes to git