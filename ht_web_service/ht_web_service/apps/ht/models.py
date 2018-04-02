from django.db import models
from ht_web_service.users.models import User as CustomUser


class Feature(models.Model):
    district = models.CharField(max_length=50, blank=True, null=True, verbose_name="district")
    order = models.CharField(max_length=256, blank=True, null=True, verbose_name="order")
    event = models.CharField(max_length=256, blank=True, null=True, verbose_name="event")
    piquetu = models.CharField(max_length=256, blank=True, null=True, verbose_name="piquetu")
    plot = models.CharField(max_length=256, blank=True, null=True, verbose_name="plot")
    rights_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="rights_14")
    rights_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="rights_17")
    cadastral_num_origin_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="cadastral_num_origin_14")
    cadastral_num_origin_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="cadastral_num_origin_17")
    origin_area_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="origin_area_17")
    vac_area_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="vac_area_14")
    vac_area_17 = models.CharField(max_length=256, blank=True, null=True, verbose_name="vac_area_17")
    category_origin = models.CharField(max_length=256, blank=True, null=True, verbose_name="category_origin")
    obj_type_origin = models.CharField(max_length=256, blank=True, null=True, verbose_name="obj_type_origin")
    cadastral_num_formed = models.CharField(max_length=256, blank=True, null=True, verbose_name="cadastral_num_formed")
    provision_doc = models.CharField(max_length=256, blank=True, null=True, verbose_name="provision_doc")
    requisites_dir_vac = models.CharField(max_length=256, blank=True, null=True, verbose_name="requisites_dir_vac")
    requisites_assess = models.CharField(max_length=256, blank=True, null=True, verbose_name="requisites_assess")
    obj_costat = models.CharField(max_length=256, blank=True, null=True, verbose_name="obj_costat")
    offer_to_holdering = models.CharField(max_length=256, blank=True, null=True, verbose_name="offer_to_holdering")
    requisites_agree_vac = models.CharField(max_length=256, blank=True, null=True, verbose_name="requisites_agree_vac")
    pre_doc_transfer_type = models.CharField(max_length=256, blank=True, null=True, verbose_name="pre_doc_transfer_type")
    requisites_lease = models.CharField(max_length=256, blank=True, null=True, verbose_name="requisites_lease")
    requisites_lease_agree = models.CharField(max_length=256, blank=True, null=True, verbose_name="requisites_lease_agree")
    contacts_holder = models.CharField(max_length=256, blank=True, null=True, verbose_name="contacts_holder")
    comments = models.CharField(max_length=256, blank=True, null=True, verbose_name="comments")
    form_area = models.CharField(max_length=256, blank=True, null=True, verbose_name="form_area")
    status_area = models.CharField(max_length=256, blank=True, null=True, verbose_name="status_area")
    rights_august_14 = models.CharField(max_length=256, blank=True, null=True, verbose_name="rights_august_14")
    pre_lang_plan = models.CharField(max_length=256, blank=True, null=True, verbose_name="pre_lang_plan")


class History(models.Model):
    date = models.DateTimeField()
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=20)
    value = models.CharField(max_length=256)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}|{1}|{2}|{3}'.format(str(self.attribute), str(self.feature.id), str(self.user.id), str(self.date))


def get_attributes():
    machine_and_verbose_names_dict = dict()
    feature_fields = Feature._meta.get_fields()
    for field in feature_fields:
        try:
            machine_and_verbose_names_dict[field.name] = field.verbose_name
        except Exception as e:
            print(e)

    return machine_and_verbose_names_dict
