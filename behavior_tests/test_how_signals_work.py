import pytest
from PySide6.QtCore import Slot, QObject, Signal


@pytest.mark.documenting_behavior
class TestHowSignalsWork:
    # NOTE: These tests are for documentation purposes only

    @pytest.fixture()
    def create_receiver(self):
        class Receiver:
            def __init__(self, signal_to_receive):
                self.signals_received = []
                signal_to_receive.connect(self.on_signal_received)

            @Slot(str)
            def on_signal_received(self, value: str) -> None:
                self.signals_received.append(value)

        return Receiver

    def test_what_happens_when_a_signal_is_attached_to_a_class(self, create_receiver):
        class Sender(QObject):
            signal: Signal = Signal(str)

            def emit_signal(self) -> None:
                self.signal.emit("a test signal was sent")

        sender = Sender()
        sender_signal = sender.signal
        receiver = create_receiver(sender_signal)

        assert receiver.signals_received == [], "The receiver should not have received any signals yet"

        sender.emit_signal()

        assert receiver.signals_received == ["a test signal was sent"], "The receiver should have received the signal"

    def test_what_happens_when_a_signal_is_attached_to_an_instance(self, create_receiver):
        class Sender(QObject):

            def __init__(self):
                super().__init__()
                self.signal: Signal = Signal(str)

            def emit_signal(self) -> None:
                self.signal.emit("a test signal was sent")

        sender = Sender()
        sender_signal = sender.signal

        with pytest.raises(AttributeError, match="object has no attribute 'connect'"):
            receiver = create_receiver(sender_signal), (
                "Expected an AttributeError because signal was incorrectly used as an instance attribute "
                "rather than a class attribute"
            )

    def test_what_happens_when_a_signal_is_attached_to_a_class_that_is_instantiated_twice(self, create_receiver):
        class Sender(QObject):
            signal: Signal = Signal(str)

            def emit_signal(self) -> None:
                self.signal.emit("a test signal was sent")

        sender1 = Sender()
        sender2 = Sender()

        sender1_signal = sender1.signal
        sender2_signal = sender2.signal

        assert sender1_signal is not sender2_signal, "The signals should be different instances"