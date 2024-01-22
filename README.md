## run test

```bash
poetry install
poetry run pytest tests
```

## pytest output

```python
cls = <class 'fullycontrolledinput.fullycontrolledinput.State'>, kwargs = {}, is_testing_env = False
parent_state = <class 'reflex_integration_import_state.state.ReuseableAppState'>

    @classmethod
    def __init_subclass__(cls, **kwargs):
        """Do some magic for the subclass initialization.

        Args:
            **kwargs: The kwargs to pass to the pydantic init_subclass method.

        Raises:
            ValueError: If a substate class shadows another.
        """
        is_testing_env = constants.PYTEST_CURRENT_TEST in os.environ
        super().__init_subclass__(**kwargs)
        # Event handlers should not shadow builtin state methods.
        cls._check_overridden_methods()

        # Reset subclass tracking for this class.
        cls.class_subclasses = set()

        # Get the parent vars.
        parent_state = cls.get_parent_state()
        if parent_state is not None:
            cls.inherited_vars = parent_state.vars
            cls.inherited_backend_vars = parent_state.backend_vars

            # Check if another substate class with the same name has already been defined.
            if cls.__name__ in set(c.__name__ for c in parent_state.class_subclasses):
                if is_testing_env:
                    # Clear existing subclass with same name when app is reloaded via
                    # utils.prerequisites.get_app(reload=True)
                    parent_state.class_subclasses = set(
                        c
                        for c in parent_state.class_subclasses
                        if c.__name__ != cls.__name__
                    )
                else:
                    # During normal operation, subclasses cannot have the same name, even if they are
                    # defined in different modules.
>                   raise ValueError(
                        f"The substate class '{cls.__name__}' has been defined multiple times. "
                        "Shadowing substate classes is not allowed."
                    )
E                   ValueError: The substate class 'State' has been defined multiple times. Shadowing substate classes is not allowed.

../reflex/reflex/state.py:308: ValueError
```
