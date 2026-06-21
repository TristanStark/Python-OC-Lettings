from django.db import migrations


def copy_old_lettings_data(apps, schema_editor):
    Address = apps.get_model('lettings', 'Address')
    Letting = apps.get_model('lettings', 'Letting')

    connection = schema_editor.connection
    existing_tables = connection.introspection.table_names()

    old_address_table = 'oc_lettings_site_address'
    old_letting_table = 'oc_lettings_site_letting'

    if old_address_table not in existing_tables:
        return

    if old_letting_table not in existing_tables:
        return

    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                id,
                number,
                street,
                city,
                state,
                zip_code,
                country_iso_code
            FROM oc_lettings_site_address
            '''
        )

        for row in cursor.fetchall():
            Address.objects.update_or_create(
                id=row[0],
                defaults={
                    'number': row[1],
                    'street': row[2],
                    'city': row[3],
                    'state': row[4],
                    'zip_code': row[5],
                    'country_iso_code': row[6],
                }
            )

        cursor.execute(
            '''
            SELECT
                id,
                title,
                address_id
            FROM oc_lettings_site_letting
            '''
        )

        for row in cursor.fetchall():
            Letting.objects.update_or_create(
                id=row[0],
                defaults={
                    'title': row[1],
                    'address_id': row[2],
                }
            )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_old_lettings_data,
            reverse_code=migrations.RunPython.noop
        ),
    ]