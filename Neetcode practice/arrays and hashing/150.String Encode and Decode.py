class Solution:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            encoded_str += f'{len(s)}#{s}'
        return encoded_str

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            decoded_strs.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

        return decoded_strs
