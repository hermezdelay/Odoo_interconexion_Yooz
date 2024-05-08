from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
import requests

_logger = logging.getLogger(__name__)


# class chargementFournisseur(models.Model):
class fournisseur_chargement_zeendoc(models.Model):
    _inherit = "res.partner"

    def synchronisation_function(self):
        # suppliers = self.env['res.partner'].search([("supplier_rank",">",0)])
        # length = suppliers.length()
        # for supplier in suppliers
        #    message2 = message2 + str(supplier.city) + "/ Supplyer "

        name = "  name = " + str(self.display_name)
        city = " city = " + str(self.city)
        country = " country = " + str(self.country_id)
        reference = " reference = " + str(self.ref)
        siret = " siret = " + str(self.siret)
        phone = " phone = " + str(self.phone)
        email = " email = " + str(self.email)
        zip = " zip = " + str(self.zip)
        id = " id = " + str(self.id)

        url = "https://geo.api.gouv.fr/communes?"
        params = {
            'codePostal': '78000'
        }
        reponse = requests.get(url, params=params)
        # message = "Mise-a-jour avec succes : " + str(reponse.json())
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': id + name + city + country + reference + siret + phone + email + zip,
                'type': 'success',
                'sticky': False,
            }
        }

        # res = super().create(vals)

        # ValidationError(_('voulez-vous vraiment ?'))

        # {'search_default_supplier': 1,'res_partner_search_mode': 'supplier', 'default_is_company': True, 'default_supplier_rank': 1}
        # [["supplier_rank",">",0]]

        # return res


