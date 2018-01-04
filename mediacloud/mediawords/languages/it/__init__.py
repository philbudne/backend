from mediawords.languages import SpaceSeparatedWordsMixIn, SentenceSplitterMixIn, PyStemmerMixIn, StopWordsFromFileMixIn


class ItalianLanguage(SpaceSeparatedWordsMixIn, SentenceSplitterMixIn, PyStemmerMixIn, StopWordsFromFileMixIn):
    """Italian language support module."""

    @staticmethod
    def language_code() -> str:
        return "it"
