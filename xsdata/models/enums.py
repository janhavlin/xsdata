from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Iterable
from typing import Optional

from lxml.etree import QName

COMMON_SCHEMA_DIR = Path(__file__).absolute().parent.parent.joinpath("schemas/")


class Namespace(Enum):
    """Common namespaces."""

    XS = "http://www.w3.org/2001/XMLSchema"
    XML = "http://www.w3.org/XML/1998/namespace"
    XSI = "http://www.w3.org/2001/XMLSchema-instance"
    XLINK = "http://www.w3.org/1999/xlink"
    XHTML = "http://www.w3.org/1999/xhtml"
    SOAP11 = "http://schemas.xmlsoap.org/wsdl/soap/"
    SOAP12 = "http://schemas.xmlsoap.org/wsdl/soap12/"

    @property
    def uri(self) -> str:
        return self.value

    @property
    def prefix(self) -> str:
        return self.name.lower()

    @property
    def location(self) -> Optional[str]:
        local_path = COMMON_SCHEMA_DIR.joinpath(f"{self.prefix}.xsd")
        return local_path.as_uri() if local_path.exists() else None

    @classmethod
    def get_enum(cls, uri: Optional[str]) -> Optional["Namespace"]:
        return __STANDARD_NAMESPACES__.get(uri) if uri else None


__STANDARD_NAMESPACES__ = {ns.uri: ns for ns in Namespace}


class QNames:
    """Common qualified names."""

    ALL = QName("__all__")
    XSI_NIL = QName(Namespace.XSI.uri, "nil")
    XSI_TYPE = QName(Namespace.XSI.uri, "type")


class NamespaceType:
    """
    Wildcard elements/attributes namespace types.

    :cvar ANY: elements from any namespace is allowed
    :cvar OTHER: elements from any namespace other than the parent element's namespace
    :cvar LOCAL: elements must come from no namespace
    :cvar TARGET: elements from the namespace of the parent element can be present
    """

    ANY = "##any"
    OTHER = "##other"
    LOCAL = "##local"
    TARGET = "##targetNamespace"


class FormType(Enum):
    """Element/Attribute form types."""

    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"


class Mode(Enum):
    """OpenContent mode types."""

    NONE = "none"
    SUFFIX = "suffix"
    INTERLEAVE = "interleave"


class DataType(Enum):
    """Xml data types to native python."""

    # xsdata custom any type
    QMAP = ("qmap", (QName, str))
    OBJECT = ("object", object)

    # xsd and xml data types
    ANY_ATOMIC_TYPE = ("anyAtomicType", str)
    ANY_URI = ("anyURI", str)
    ANY_SIMPLE_TYPE = ("anySimpleType", object)
    ANY_TYPE = ("anyType", object)
    BASE = ("base", str)
    BASE64_BINARY = ("base64Binary", str)
    BOOLEAN = ("boolean", bool)
    BYTE = ("byte", int)
    DATE = ("date", str)
    DATE_TIME = ("dateTime", str)
    DATE_TIMESTAMP = ("dateTimeStamp", str)
    DAY_TIME_DURATION = ("dayTimeDuration", str)
    YEAR_MONTH_DURATION = ("yearMonthDuration", str)
    DECIMAL = ("decimal", Decimal)
    DERIVATION_CONTROL = ("derivationControl", str)
    DOUBLE = ("double", Decimal)
    DURATION = ("duration", str)
    ENTITIES = ("ENTITIES", int)
    ENTITY = ("ENTITY", int)
    FLOAT = ("float", float)
    G_DAY = ("gDay", str)
    G_MONTH = ("gMonth", str)
    G_MONTH_DAY = ("gMonthDay", str)
    G_YEAR = ("gYear", str)
    G_YEAR_MONTH = ("gYearMonth", str)
    HEX_BINARY = ("hexBinary", str)
    ID = ("ID", str)
    IDREF = ("IDREF", str)
    IDREFS = ("IDREFS", str)
    INT = ("int", int)
    INTEGER = ("integer", int)
    LANG = ("lang", str)
    LANGUAGE = ("language", str)
    LONG = ("long", int)
    NAME = ("Name", str)
    NCNAME = ("NCName", str)
    NEGATIVE_INTEGER = ("negativeInteger", int)
    NMTOKEN = ("NMTOKEN", str)
    NMTOKENS = ("NMTOKENS", str)
    NON_NEGATIVE_INTEGER = ("nonNegativeInteger", int)
    NON_POSITIVE_INTEGER = ("nonPositiveInteger", int)
    NORMALIZED_STRING = ("normalizedString", str)
    NOTATION = ("NOTATION", str)
    POSITIVE_INTEGER = ("positiveInteger", int)
    QNAME = ("QName", QName)
    SHORT = ("short", int)
    SIMPLE_DERIVATION_SET = ("simpleDerivationSet", str)
    STRING = ("string", str)
    TIME = ("time", str)
    TOKEN = ("token", str)
    UNSIGNED_BYTE = ("unsignedByte", int)
    UNSIGNED_INT = ("unsignedInt", int)
    UNSIGNED_LONG = ("unsignedLong", int)
    UNSIGNED_SHORT = ("unsignedShort", int)

    def __init__(self, code: str, local: type):
        self.code = code
        self.local = local

    @property
    def qname(self) -> QName:
        return QName(Namespace.XS.uri, self.code)

    @property
    def local_name(self) -> str:
        if isinstance(self.local, Iterable):
            return ", ".join([local.__name__ for local in self.local])

        return self.local.__name__

    @classmethod
    def get_enum(cls, code: str) -> Optional["DataType"]:
        return __XSDType__.get(code) if code else None


__XSDType__ = {xsd.code: xsd for xsd in DataType}


class EventType:
    """XmlParsing event types."""

    START = "start"
    START_NS = "start-ns"
    END = "end"


class Tag:
    """Xml Schema tag names."""

    ALL = "All"
    ANNOTATION = "Annotation"
    ANY = "Any"
    ANY_ATTRIBUTE = "AnyAttribute"
    APPINFO = "Appinfo"
    ASSERTION = "Assertion"
    ALTERNATIVE = "Alternative"
    ATTRIBUTE = "Attribute"
    ATTRIBUTE_GROUP = "AttributeGroup"
    CHOICE = "Choice"
    COMPLEX_CONTENT = "ComplexContent"
    COMPLEX_TYPE = "ComplexType"
    DOCUMENTATION = "Documentation"
    ELEMENT = "Element"
    EXTENSION = "Extension"
    FIELD = "Field"
    GROUP = "Group"
    IMPORT = "Import"
    INCLUDE = "Include"
    KEY = "Key"
    KEYREF = "Keyref"
    LIST = "List"
    NOTATION = "Notation"
    OVERRIDE = "Override"
    REDEFINE = "Redefine"
    RESTRICTION = "Restriction"
    SCHEMA = "Schema"
    SELECTOR = "Selector"
    SEQUENCE = "Sequence"
    SIMPLE_CONTENT = "SimpleContent"
    SIMPLE_TYPE = "SimpleType"
    UNION = "Union"
    UNIQUE = "Unique"

    # Restrictions
    ENUMERATION = "Enumeration"
    FRACTION_DIGITS = "FractionDigits"
    LENGTH = "Length"
    MAX_EXCLUSIVE = "MaxExclusive"
    MAX_INCLUSIVE = "MaxInclusive"
    MAX_LENGTH = "MaxLength"
    MIN_EXCLUSIVE = "MinExclusive"
    MIN_INCLUSIVE = "MinInclusive"
    MIN_LENGTH = "MinLength"
    PATTERN = "Pattern"
    TOTAL_DIGITS = "TotalDigits"
    WHITE_SPACE = "WhiteSpace"


class UseType(Enum):
    """Attribute use types."""

    OPTIONAL = "optional"
    PROHIBITED = "prohibited"
    REQUIRED = "required"


class ProcessType(Enum):
    """Wildcard process types."""

    LAX = "lax"
    SKIP = "skip"
    STRICT = "strict"


class BindingStyle(Enum):
    RPC = "rpc"
    DOCUMENT = "document"


class UseChoice(Enum):
    LITERAL = "literal"
    ENCODED = "encoded"
