# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/data/ProgramStatus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/data/ProgramStatus.proto',
  package='dwango.nicolive.chat.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-dwango/nicolive/chat/data/ProgramStatus.proto\x12\x19\x64wango.nicolive.chat.data\"o\n\rProgramStatus\x12=\n\x05state\x18\x01 \x01(\x0e\x32..dwango.nicolive.chat.data.ProgramStatus.State\"\x1f\n\x05State\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05\x45nded\x10\x01\x62\x06proto3')
)



_PROGRAMSTATUS_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='dwango.nicolive.chat.data.ProgramStatus.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ended', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=156,
  serialized_end=187,
)
_sym_db.RegisterEnumDescriptor(_PROGRAMSTATUS_STATE)


_PROGRAMSTATUS = _descriptor.Descriptor(
  name='ProgramStatus',
  full_name='dwango.nicolive.chat.data.ProgramStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='dwango.nicolive.chat.data.ProgramStatus.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROGRAMSTATUS_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=187,
)

_PROGRAMSTATUS.fields_by_name['state'].enum_type = _PROGRAMSTATUS_STATE
_PROGRAMSTATUS_STATE.containing_type = _PROGRAMSTATUS
DESCRIPTOR.message_types_by_name['ProgramStatus'] = _PROGRAMSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProgramStatus = _reflection.GeneratedProtocolMessageType('ProgramStatus', (_message.Message,), dict(
  DESCRIPTOR = _PROGRAMSTATUS,
  __module__ = 'dwango.nicolive.chat.data.ProgramStatus_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.ProgramStatus)
  ))
_sym_db.RegisterMessage(ProgramStatus)


# @@protoc_insertion_point(module_scope)
