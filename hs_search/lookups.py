__author__ = 'aamir'


from ajax_select import LookupChannel

# class HS4Lookup(LookupChannel):
#
#     model = itc_hs4
#
#     def get_query(self, q, request):
#         # import pdb
#         # pdb.set_trace()
#         print '*'*100
#         print request.COOKIES
#         return self.model.objects.filter(desc__icontains=q)
#
#     def get_result(self, obj):
#         return unicode(obj.desc)
#
#
#
# class HS8Lookup(LookupChannel):
#
#     model = itc_hs8
#
#     def get_query(self, q, request):
#
#         return self.model.objects.filter(desc__icontains=q)
#
#     def get_result(self, obj):
#         return unicode(obj.desc)