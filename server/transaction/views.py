from rest_framework import response, decorators as rest_decorators, permissions as rest_permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='post',
    responses={
        200: openapi.Response(
            description="Payment successful",
            examples={
                "application/json": {
                    "msg": "Success"
                }
            }
        ),
        401: openapi.Response(description="Unauthorized"),
    },
    operation_description="Process the subscription payment for the authenticated user",
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    return response.Response({"msg": "Success"}, 200)

@swagger_auto_schema(
    method='post',
    responses={
        200: openapi.Response(
            description="Subscriptions retrieved successfully",
            examples={
                "application/json": {
                    "msg": "Success"
                }
            }
        ),
        401: openapi.Response(description="Unauthorized"),
    },
    operation_description="List all subscriptions for the authenticated user",
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    return response.Response({"msg": "Success"}, 200)
