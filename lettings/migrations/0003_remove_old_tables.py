from django.db import migrations


def remove_old_tables(apps, schema_editor):
    connection = schema_editor.connection
    existing_tables = connection.introspection.table_names()

    old_tables = [
        'oc_lettings_site_letting',
        'oc_lettings_site_address',
        'oc_lettings_site_profile',
    ]

    for table_name in old_tables:
        if table_name in existing_tables:
            schema_editor.execute(
                'DROP TABLE IF EXISTS "{table_name}"'.format(
                    table_name=table_name
                )
            )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_copy_old_data'),
        ('profiles', '0002_copy_old_data'),
    ]

    operations = [
        migrations.RunPython(
            remove_old_tables,
            reverse_code=migrations.RunPython.noop
        ),
    ]