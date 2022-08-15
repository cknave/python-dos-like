#!/usr/bin/env python
#
# Create a custom intersphinx mapping object inventory to link
# _cffi_backend._CDataBase to the relevant section of the CFFI docs.
#
# Is there a better way to do this?  If there is, Google has failed me!
#
# pip install sphobjinv
#
import sphobjinv

inv = sphobjinv.Inventory()
inv.project = 'cffi'
inv.version = '1.15.1'
inv.objects.append(sphobjinv.DataObjStr(
    name='_cffi_backend._CDataBase',
    domain='py',
    role='class',
    priority='1',
    uri='ref.html#ffi-cdata-ffi-ctype',
    dispname='CData'))

result = sphobjinv.compress(inv.data_file())
with open('cffi-cdata.inv', 'wb') as f:
    f.write(result)
