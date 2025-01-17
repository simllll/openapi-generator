# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class NullableClass(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class integer_prop(
        _SchemaTypeChecker(typing.Union[none_type, decimal.Decimal, ]),
        IntBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[int, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'integer_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class number_prop(
        _SchemaTypeChecker(typing.Union[none_type, decimal.Decimal, ]),
        NumberBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[float, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'number_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class boolean_prop(
        _SchemaTypeChecker(typing.Union[none_type, bool, ]),
        BoolBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[bool, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'boolean_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class string_prop(
        _SchemaTypeChecker(typing.Union[none_type, str, ]),
        StrBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[str, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'string_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class date_prop(
        _SchemaTypeChecker(typing.Union[none_type, str, ]),
        DateBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'date_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class datetime_prop(
        _SchemaTypeChecker(typing.Union[none_type, str, ]),
        DateTimeBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'datetime_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class array_nullable_prop(
        _SchemaTypeChecker(typing.Union[tuple, none_type, ]),
        ListBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[list, tuple, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'array_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class array_and_items_nullable_prop(
        _SchemaTypeChecker(typing.Union[tuple, none_type, ]),
        ListBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[list, tuple, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'array_and_items_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
    class array_items_nullable(
        ListSchema
    ):
        
        
        class _items(
            _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
            DictBase,
            NoneBase,
            Schema
        ):
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict, None, ],
                _configuration: typing.Optional[Configuration] = None,
                **kwargs: typing.Type[Schema],
            ) -> '_items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    
    class object_nullable_prop(
        _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
        DictBase,
        NoneBase,
        Schema
    ):
        _additional_properties = DictSchema
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'object_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class object_and_items_nullable_prop(
        _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
        DictBase,
        NoneBase,
        Schema
    ):
        
        
        class _additional_properties(
            _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
            DictBase,
            NoneBase,
            Schema
        ):
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict, None, ],
                _configuration: typing.Optional[Configuration] = None,
                **kwargs: typing.Type[Schema],
            ) -> '_additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'object_and_items_nullable_prop':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class object_items_nullable(
        DictSchema
    ):
        
        
        class _additional_properties(
            _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
            DictBase,
            NoneBase,
            Schema
        ):
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict, None, ],
                _configuration: typing.Optional[Configuration] = None,
                **kwargs: typing.Type[Schema],
            ) -> '_additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'object_items_nullable':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class _additional_properties(
        _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
        DictBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> '_additional_properties':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        integer_prop: typing.Union[integer_prop, Unset] = unset,
        number_prop: typing.Union[number_prop, Unset] = unset,
        boolean_prop: typing.Union[boolean_prop, Unset] = unset,
        string_prop: typing.Union[string_prop, Unset] = unset,
        date_prop: typing.Union[date_prop, Unset] = unset,
        datetime_prop: typing.Union[datetime_prop, Unset] = unset,
        array_nullable_prop: typing.Union[array_nullable_prop, Unset] = unset,
        array_and_items_nullable_prop: typing.Union[array_and_items_nullable_prop, Unset] = unset,
        array_items_nullable: typing.Union[array_items_nullable, Unset] = unset,
        object_nullable_prop: typing.Union[object_nullable_prop, Unset] = unset,
        object_and_items_nullable_prop: typing.Union[object_and_items_nullable_prop, Unset] = unset,
        object_items_nullable: typing.Union[object_items_nullable, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'NullableClass':
        return super().__new__(
            cls,
            *args,
            integer_prop=integer_prop,
            number_prop=number_prop,
            boolean_prop=boolean_prop,
            string_prop=string_prop,
            date_prop=date_prop,
            datetime_prop=datetime_prop,
            array_nullable_prop=array_nullable_prop,
            array_and_items_nullable_prop=array_and_items_nullable_prop,
            array_items_nullable=array_items_nullable,
            object_nullable_prop=object_nullable_prop,
            object_and_items_nullable_prop=object_and_items_nullable_prop,
            object_items_nullable=object_items_nullable,
            _configuration=_configuration,
            **kwargs,
        )
