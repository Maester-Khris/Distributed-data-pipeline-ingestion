from .employee_controller import employee_bp
from .message_controller import message_bp
from .kafka_controller import kafka_bp
from .remote_controller import remote_bp

__all__ = [
    'employee_bp',
    'message_bp',
    'kafka_bp',
    'remote_bp'
]