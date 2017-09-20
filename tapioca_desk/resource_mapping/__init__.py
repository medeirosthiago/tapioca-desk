from .cases import CASES_MAPPING
from .labels import LABELS_MAPPING
from .customers import CUSTOMERS_MAPPING
from .companies import COMPANIES_MAPPING

RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(CASES_MAPPING)
RESOURCE_MAPPING.update(LABELS_MAPPING)
RESOURCE_MAPPING.update(CUSTOMERS_MAPPING)
RESOURCE_MAPPING.update(COMPANIES_MAPPING)
