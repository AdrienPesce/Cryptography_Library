#!/usr/bin/python3.5

# ################################################################################################################################
# 		 Notes
# ################################################################################################################################

'''

Module sha

Used to get the hash of a message using the Secure Hash Algorithm

In this module, the algorithms implemeted are:
    - SHA-256
    - SHA-512

'''



# ################################################################################################################################
#       Import modules
# ################################################################################################################################

# Standard modules
from abc import ABC, abstractmethod



# ################################################################################################################################
# 		 Classes
# ################################################################################################################################

# ################################################################
# 		 SHA256
# ################################################################

class SHA256(ABC):
    ''' Class to get the hash of a message using SHA-256

        Attributes
        ----------
        
        Methods
        -------
            
        Examples
        --------
            hashMethod = SHA256()
            hashValue = hashMethod.get_hash('test')
            print(hashValue)

        '''

    def __init__(self):
        ''' Initialize the attributes '''
        self._initialize_hash_values()
        self._initialize_round_constants()


    def _initialize_hash_values(self):
        ''' Initialize the hash values h0 to h7 '''
        pass

    
    def _initialize_round_constants(self):
        ''' Initialize the round constants K0 to K63 '''
        pass


    def get_hash(self, message):
        ''' Return the hash value of the message using SHA-256

            Parameters
            ----------
                message : str
                    Message to get the hash of
      
            Returns
            -------
                hashedMessage : str
                    Hash of the message

            '''
        message = self._pre_processing(message)
        chunks = self._get_chunks(message)
        for chunk in chunks:
            words = self._get_words(chunk)
            wh = self._get_working_variables()
            wh = self._compression_loop(words, wh)
            self._add_compressed_chunk_to_current_hash_value(wh)

        hashedMessage = self._produce_final_hash()
        return str(hashedMessage)

    
    def _pre_processing(self, message):
        ''' Get the message with a lentgh L, add bits to reach the block size and return it

            Parameters
            ----------
                message : str
                    Message to get the hash of with a length L
      
            Returns
            -------
                message : bytes
                    Message to get the hash of with a lentgh equal to a multiple of the block size

            '''
        return message


    def _get_chunks(self, message):
        ''' Break message into (block size)-bit chunks and return them

            Parameters
            ----------
                message : str
                    Message to get the hash of
      
            Returns
            -------
                chunks : list
                    List of (block size) bits chunks

            '''
        chunks = []
        return chunks


    def _get_words(self, chunk):
        ''' Create first words by splitting chunk into (word-size)-bit words and 
                extend the first words into the remaining ones

            Parameters
            ----------
                chunk : bytes
                    Message to get the hash of
      
            Returns
            -------
                words : list
                    List of (word-size) bites words

            '''
        words = []
        return words


    def _get_working_variables(self):
        ''' Return working hash variables

            Returns
            -------
                wh : list
                    List containing the current hash values

            '''
        wh = []
        return wh


    def _compression_loop(self, words, wh):
        ''' Return the hash value of the message using SHA-256

            Parameters
            ----------
                words : list
                    List of (word-size) bites words
                wh : list
                    List containing the current hash values
      
            Returns
            -------
                wh : list
                    List containing the current hash values

            '''
        return wh


    def _add_compressed_chunk_to_current_hash_value(self, wh):
        ''' Add the compressed chunk to the current hash value

            Parameters
            ----------
                wh : list
                    List containing the current hash values
      
            '''
        pass


    def _produce_final_hash(self):
        ''' Produce the final hash computation

            Returns
            -------
                hashedMessage : bytes
                    Hash of the message

            '''
        hashedMessage = None
        return hashedMessage 


# ################################################################
# 		 SHA512
# ################################################################

class SHA512(SHA256):
    ''' Class to get the hash of a message using SHA-512

        Attributes
        ----------
        
        Methods
        -------
            
        Examples
        --------
            hashMethod = SHA512()
            hashValue = hashMethod.get_hash('test')
            print(hashValue)

        '''

    def __init__(self):
        ''' Initialize the attributes '''
        self._initialize_hash_values()
        self._initialize_round_constants()


    def _initialize_hash_values(self):
        ''' Initialize the hash values h0 to h7 '''
        pass

    
    def _initialize_round_constants(self):
        ''' Initialize the round constants K0 to K79 '''
        pass



# ################################################################################################################################
# 		 Main
# ################################################################################################################################

if __name__ == '__main__':
    hashMethod = SHA512()
    hashValue = hashMethod.get_hash('test')
    print(hashValue)