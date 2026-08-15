def pre_init(env):
    query = """
        UPDATE ir_ui_view
        SET arch_db = jsonb_strip_nulls(jsonb_set(arch_db, '{id_ID}', 'null'))
        WHERE name IN ('res.company.form', 'res.partner.form');
    """
    env.cr.execute(query)
