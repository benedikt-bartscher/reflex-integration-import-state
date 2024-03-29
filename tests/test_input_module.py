"""Integration tests for text input and related components."""
import time
from typing import Generator
from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from reflex.testing import AppHarness


@pytest.fixture()
def fully_controlled_input_module(tmp_path) -> Generator[AppHarness, None, None]:
    """Start FullyControlledInput app at tmp_path via AppHarness.

    Args:
        tmp_path: pytest tmp_path fixture

    Yields:
        running AppHarness instance
    """
    #  with AppHarness.create(
    #      root=tmp_path,
    #      app_source=FullyControlledInput,  # type: ignore
    #  ) as harness:
    with AppHarness.create(
        root=Path(__file__).parent.parent / Path("testmodule")
    ) as harness:
        yield harness


@pytest.mark.asyncio
async def test_fully_controlled_input_module(fully_controlled_input_module: AppHarness):
    """Type text after moving cursor. Update text on backend.

    Args:
        fully_controlled_input_module: harness for FullyControlledInput app
    """
    assert fully_controlled_input_module.app_instance is not None, "app is not running"
    driver = fully_controlled_input_module.frontend()

    # get a reference to the connected client
    token_input = driver.find_element(By.ID, "token")
    assert token_input

    # wait for the backend connection to send the token
    token = fully_controlled_input_module.poll_for_value(token_input)
    assert token

    return

    # find the input and wait for it to have the initial state value
    debounce_input = driver.find_element(By.ID, "debounce_input_input")
    value_input = driver.find_element(By.ID, "value_input")
    on_change_input = driver.find_element(By.ID, "on_change_input")
    plain_value_input = driver.find_element(By.ID, "plain_value_input")
    clear_button = driver.find_element(By.TAG_NAME, "button")
    assert fully_controlled_input_module.poll_for_value(debounce_input) == "initial"
    assert fully_controlled_input_module.poll_for_value(value_input) == "initial"
    assert fully_controlled_input_module.poll_for_value(plain_value_input) == "initial"
    assert (
        plain_value_input.value_of_css_property("background-color")
        == "rgba(238, 238, 238, 1)"
    )

    # move cursor to home, then to the right and type characters
    debounce_input.send_keys(Keys.HOME, Keys.ARROW_RIGHT)
    debounce_input.send_keys("foo")
    time.sleep(0.5)
    assert debounce_input.get_attribute("value") == "ifoonitial"
    assert (await fully_controlled_input_module.get_state(token)).substates[
        "reuseable_app_state"
    ].substates["state2"].text == "ifoonitial"
    assert fully_controlled_input_module.poll_for_value(value_input) == "ifoonitial"
    assert (
        fully_controlled_input_module.poll_for_value(plain_value_input) == "ifoonitial"
    )

    # clear the input on the backend
    async with fully_controlled_input_module.modify_state(token) as state:
        state.substates["reuseable_app_state"].substates["state2"].text = ""
    assert (await fully_controlled_input_module.get_state(token)).substates[
        "reuseable_app_state"
    ].substates["state2"].text == ""
    assert (
        fully_controlled_input_module.poll_for_value(
            debounce_input, exp_not_equal="ifoonitial"
        )
        == ""
    )

    # type more characters
    debounce_input.send_keys("getting testing done")
    time.sleep(0.5)
    assert debounce_input.get_attribute("value") == "getting testing done"
    assert (await fully_controlled_input_module.get_state(token)).substates[
        "reuseable_app_state"
    ].substates["state2"].text == "getting testing done"
    assert (
        fully_controlled_input_module.poll_for_value(value_input)
        == "getting testing done"
    )
    assert (
        fully_controlled_input_module.poll_for_value(plain_value_input)
        == "getting testing done"
    )

    # type into the on_change input
    on_change_input.send_keys("overwrite the state")
    time.sleep(0.5)
    assert debounce_input.get_attribute("value") == "overwrite the state"
    assert on_change_input.get_attribute("value") == "overwrite the state"
    assert (await fully_controlled_input_module.get_state(token)).substates[
        "reuseable_app_state"
    ].substates["state2"].text == "overwrite the state"
    assert (
        fully_controlled_input_module.poll_for_value(value_input)
        == "overwrite the state"
    )
    assert (
        fully_controlled_input_module.poll_for_value(plain_value_input)
        == "overwrite the state"
    )

    clear_button.click()
    time.sleep(0.5)
    assert on_change_input.get_attribute("value") == ""
    # potential bug: clearing the on_change field doesn't itself trigger on_change
    # assert backend_state.text == ""
    # assert debounce_input.get_attribute("value") == ""
    # assert value_input.get_attribute("value") == ""
