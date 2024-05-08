<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="fournisseur_view" model="ir.ui.view">
        <field name="name">fournisseur.view</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_tree"/>
        <field name="arch" type="xml">
            <xpath expr="synchronisation_function" position="after">
                <header>
                    <button name="Synchronisation_function" type="object" string="Synchroniser" class="btn-primary"/>
                </header>
            </xpath>
        </field>
    </record>
</odoo>