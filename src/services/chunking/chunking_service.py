from langchain_text_splitters import CharacterTextSplitter
from src.domain.repositories.chunker import ChunkerText

class ChunkDocuments(ChunkerText):

    def __init__(self):
        self.chunk_loader = self.__config_chunker_params()


    def __config_chunker_params(self):
        return CharacterTextSplitter.from_tiktoken_encoder(
            encoding_name='cl100k_base',
            chunk_size=200,
            chunk_overlap=0
        )

    def chunk(self, text):
        texts = self.chunk_loader.split_text(text)
        return texts
