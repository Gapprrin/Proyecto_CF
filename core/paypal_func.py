# pip install paypal-server-sdk==0.5.1

import logging
import os

from flask import Flask, request
from paypalserversdk.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from paypalserversdk.logging.configuration.api_logging_configuration import (
    LoggingConfiguration,
    RequestLoggingConfiguration,
    ResponseLoggingConfiguration,
)
from paypalserversdk.paypalserversdk_client import PaypalserversdkClient
from paypalserversdk.controllers.orders_controller import OrdersController
from paypalserversdk.controllers.payments_controller import PaymentsController
from paypalserversdk.models.amount_with_breakdown import AmountWithBreakdown
from paypalserversdk.models.checkout_payment_intent import CheckoutPaymentIntent
from paypalserversdk.models.order_request import OrderRequest
from paypalserversdk.models.capture_request import CaptureRequest
from paypalserversdk.models.money import Money
from paypalserversdk.models.shipping_details import ShippingDetails
from paypalserversdk.models.shipping_option import ShippingOption
from paypalserversdk.models.shipping_type import ShippingType
from paypalserversdk.models.purchase_unit_request import PurchaseUnitRequest
from paypalserversdk.models.payment_source import PaymentSource
from paypalserversdk.models.card_request import CardRequest
from paypalserversdk.models.card_attributes import CardAttributes
from paypalserversdk.models.card_verification import CardVerification
from paypalserversdk.models.card_verification_method import CardVerificationMethod
from paypalserversdk.api_helper import ApiHelper


# Aquí genero en la variable "cliente" el token de acceso
client = PaypalserversdkClient(
    # acá establesco las credenciales del cliente (en este caso es la cuenta buisness)
    client_credentials_auth_credentials= ClientCredentialsAuthCredentials(
        o_auth_client_id="ARnmuLydZhMSl-ZvDIjgig9jdJhNq-QIOETql1rgXTq_hIkEiDk_U5aKWMSuoEqd52xAgT0g05k-eySv",
        o_auth_client_secret="EFa2bbFILN6XqAefV2_FvYEzsKB213HrbrPOv7tOr9N-3ORiVNFlSWfCswiyBDi-3t22dKe6PyJhNnZ8"
    ),
    # configuración del inicio de sesión que no logro entender
    logging_configuration= LoggingConfiguration(
        log_level= logging.INFO,
        mask_sensitive_headers= False,
        request_logging_config= RequestLoggingConfiguration(
            log_headers= True, log_body= True
        ),
        response_logging_config= ResponseLoggingConfiguration(
            log_headers= True, log_body= True
        )
    )
)

# view para crear la orden
# def createOrder(request):
#     if request.method == "POST":
        