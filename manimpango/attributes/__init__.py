# -*- coding: utf-8 -*-
import typing as T

from ._attributes import covert_hex_to_rbg

__all__ = ["TextAttribute"]


def _parse_color_output(val: T.Union[str, T.Iterable[int]]):
    color_hex = None
    red, green, blue = None, None, None
    if isinstance(val, str):
        color_hex = val
    else:
        if len(val) != 3:
            raise ValueError("Either a Iterable of 3 items or a string must be passed.")
        red, green, blue = val
    if color_hex:
        red, green, blue = covert_hex_to_rbg(color_hex)
    if not ((0 <= red <= 65535) and (0 <= green <= 65535) and (0 <= blue <= 65535)):
        raise ValueError("red, green, blue should be between 0 and 65535.")
    return (red, green, blue)


class TextAttribute:
    """:class:`TextAttribute` defines the properties/attributes of the
    text within a specific range of the text.


    A :class:`TextAttribute` object can define multiple properties at
    the same time, for example, it can change the :attr:`background_color`,
    as well as, :attr:`foreground_color`. Also, a :class:`TextAttribute` can
    be used for multiple times for different texts.
    By default, an attribute has an inclusive range from ``0`` to the
    end of the text ``-1``, ie. ``[0, -1]``.
    """

    def __init__(self, start_index: int = 0, end_index: int = -1) -> None:
        """Initialize :class:`TextAttribute`.

        Parameters
        ----------
        start_index : int, optional
            The start index of the range, by default 0 (start of the string).
        end_index : int, optional
            End index of the range. The character at this index is not included
            in the range, by default -1 (end of the string).
        """
        self.start_index = start_index
        self.end_index = end_index

    @property
    def start_index(self) -> int:
        """It is the end index of the range.

        Raises
        ------
        ValueError
            If the value is not an :class:`int`.
        """
        return self._start_index

    @start_index.setter
    def start_index(self, val: int) -> None:
        if not isinstance(val, int):
            raise ValueError("'start_index' should be an int")
        self._start_index = val

    @property
    def end_index(self) -> int:
        """It is the start of the range. The character at this index is not
        included in the range.

        Raises
        ------
        ValueError
            If the value is not an :class:`int`.
        """
        return self._end_index

    @end_index.setter
    def end_index(self, val: int) -> None:
        if not isinstance(val, int):
            raise ValueError("'end_index' should be an int")
        self._end_index = val

    @property
    def allow_breaks(self) -> T.Union[bool, None]:
        """Whether to break text or not.

        If breaks are disabled, the range will be kept in a single run,
        as far as possible.
        """
        if hasattr(self, "_allow_breaks"):
            return self._allow_breaks
        return None

    @allow_breaks.setter
    def allow_breaks(self, val: bool) -> None:
        self._allow_breaks = bool(val)

    @property
    def background_alpha(self) -> float:
        """The background_alpha of the text.

        Raises
        ------
        ValueError
            If the value is not between 0 and 1.
        """
        if hasattr(self, "_background_alpha"):
            return self._background_alpha
        return None

    @background_alpha.setter
    def background_alpha(self, val: float) -> None:
        if not (0 <= val <= 1):
            raise ValueError("'val' should be between 0 and 1")
        self._background_alpha = val

    @property
    def background_color(self) -> T.Union[T.Tuple[int], None]:
        """The background color of the region.

        If the input is a :class:`str` the value is considered as
        string representation of color from
        `CSS Specification <https://www.w3.org/TR/css-color-4/#named-colors>`_.
        The color is then parsed and :class:`ValueError` is raised
        if the color is invalid.

        If the input is a :class:`collections.abc.Iterable` then the items
        in them are parsed in the order of ``red, green, blue`` and checked
        whether they are valid (between 0 and 65535).


        Returns either ``None`` or a :class:`tuple` with 3 elements
        representing red, green, blue respectively. The value of each
        items in that tuple ranges from 0 to 65535.

        Raises
        ------
        ValueError
            If the value passed isn't a :class:`collections.abc.Iterable` of 3
            elements or a string. Another condition when `ValueError` is
            raised is when the color passed is invalid.

        """
        if hasattr(self, "_background_color"):
            return self._background_color
        return None

    @background_color.setter
    def background_color(self, val: T.Union[str, T.Iterable[int]]) -> None:
        self._background_color = _parse_color_output(val)

    @property
    def fallback(self) -> bool:
        """Enable or disable fallbacks.

        If fallback is disabled, characters will only be used from the
        closest matching font on the system. No fallback will be done to
        other fonts on the system that might contain the characters in
        the text.
        """
        if hasattr(self, "_fallback"):
            return self._fallback
        return None

    @fallback.setter
    def fallback(self, val: bool) -> None:
        self._fallback = bool(val)

    @property
    def family(self) -> str:
        """The font family the text should render. Can be a comma seperated
        list of fonts in a string.

        Raises
        ------
        ValueError
            If value isn't a str.
        """
        if hasattr(self, "_family"):
            return self._family
        return None

    @family.setter
    def family(self, val: str) -> None:
        if not isinstance(val, str):
            raise ValueError("'family' must be a string")
        self._family = val
