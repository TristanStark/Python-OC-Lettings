from django.db import migrations


def copy_old_profiles_data(apps, schema_editor):
    Profile = apps.get_model('profiles', 'Profile')

    connection = schema_editor.connection
    existing_tables = connection.introspection.table_names()

    old_profile_table = 'oc_lettings_site_profile'

    if old_profile_table not in existing_tables:
        return

    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                id,
                favorite_city,
                user_id
            FROM oc_lettings_site_profile
            '''
        )

        for row in cursor.fetchall():
            Profile.objects.update_or_create(
                id=row[0],
                defaults={
                    'favorite_city': row[1],
                    'user_id': row[2],
                }
            )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_old_profiles_data,
            reverse_code=migrations.RunPython.noop
        ),
    ]