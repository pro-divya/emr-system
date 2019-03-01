AMRA_TYPE = 'AMRA'
SARS_TYPE = 'SARS'

INSTRUCTION_TYPE_CHOICES = (
    (AMRA_TYPE, 'AMRA'),
    (SARS_TYPE, 'SARS')
)

INSTRUCTION_STATUS_NEW = 0
INSTRUCTION_STATUS_PROGRESS = 1
INSTRUCTION_STATUS_COMPLETE = 2
INSTRUCTION_STATUS_REJECT = 3
INSTRUCTION_STATUS_PAID = 4
INSTRUCTION_STATUS_FINALISE = 5
INSTRUCTION_STATUS_FAIL = 6

INSTRUCTION_STATUS_CHOICES = (
    (INSTRUCTION_STATUS_NEW, 'New'),
    (INSTRUCTION_STATUS_PROGRESS, 'In Progress'),
    (INSTRUCTION_STATUS_COMPLETE, 'Completed'),
    (INSTRUCTION_STATUS_REJECT, 'Rejected'),
    (INSTRUCTION_STATUS_PAID, 'Paid'),
    (INSTRUCTION_STATUS_FINALISE, 'Finalise'),
    (INSTRUCTION_STATUS_FAIL, 'Generated Fail')
)

PATIENT_NOT_FOUND = 0
PATIENT_NO_LONGER_REGISTERED = 1
CONSENT_INVALID = 2
INAPPROPRIATE_SAR = 3
GENERATOR_FAIL = 4
INSTRUCTION_REJECT_TYPE = (
    (PATIENT_NOT_FOUND, 'No suitable patient can be found'),
    (PATIENT_NO_LONGER_REGISTERED, 'The patient is no longer registered at this practice'),
    (CONSENT_INVALID, 'The consent form is invalid'),
    (INAPPROPRIATE_SAR, 'Inappropriate instruction for Subject Access Request'),
    (GENERATOR_FAIL, 'The instruction has generated fail')
)
