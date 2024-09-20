import time
import board
import pwmio

servo = pwmio.PWMOut(board.A1, frequency=50)

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

while True:
    print("1")
    servo.duty_cycle = servo_duty_cycle(1.0)
    time.sleep(1.0)
    print("0")
    servo.duty_cycle = servo_duty_cycle(0)
    time.sleep(1.0)