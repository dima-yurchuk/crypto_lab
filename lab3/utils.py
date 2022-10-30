def ukr_alphabet_to_bin(str, ukr_char_to_bin_dict):
	bin = ""
	for i in range(len(str)):
		bin = bin + ukr_char_to_bin_dict[str[i]]
	return bin


def bin_to_ukr_alphabet(str, bin_to_ukr_chracter_dict):
	ukr_str = ""
	for i in range(0, len(str), 8):
		ch = ""
		ch = ch + str[i]
		ch = ch + str[i + 1]
		ch = ch + str[i + 2]
		ch = ch + str[i + 3]
		ch = ch + str[i + 4]
		ch = ch + str[i + 5]
		ch = ch + str[i + 6]
		ch = ch + str[i + 7]
		ukr_str = ukr_str + bin_to_ukr_chracter_dict[ch]
	return ukr_str


def bin_to_dec(binary_str):
	decimal, i, n = 0, 0, 0
	while(binary_str != 0):
		dec = binary_str % 10
		decimal = decimal + dec * pow(2, i)
		binary_str = binary_str // 10
		i += 1
	return decimal


def dec_to_bin(num):
	res = bin(num).replace("0b", "")
	if(len(res) % 8 != 0):
		div = len(res) / 8
		div = int(div)
		counter = (8 * (div + 1)) - len(res)
		for i in range(0, counter):
			res = '0' + res
	return res


def permute(input_text, permutation_arr, cout_bits):
	permutation = ""
	for i in range(0, cout_bits):
		permutation = permutation + input_text[permutation_arr[i] - 1]
	return permutation


def shift_left(bin_str, shift_number):
	s = ""
	for i in range(shift_number):
		for j in range(1, len(bin_str)):
			s = s + bin_str[j]
		s = s + bin_str[0]
		bin_str = s
		s = ""
	return bin_str

def xor(bin_str_first, bin_str_second):
	ans = ""
	for i in range(len(bin_str_first)):
		if bin_str_first[i] == bin_str_second[i]:
			ans = ans + "0"
		else:
			ans = ans + "1"
	return ans


def encrypt(input_text, round_key, initial_permutation, expand_right_to_48_arr,
			s_boxes, permutation_after_sbox, final_permutation):
	input_text = permute(input_text, initial_permutation, 64)

	left = input_text[0:32]
	right = input_text[32:64]

	for i in range(0, 16):
		# expanding the 32 bits data into 48 bits
		right_expanded = permute(right, expand_right_to_48_arr, 48)

		# XOR round rey and right_expanded
		xor_right = xor(right_expanded, round_key[i])

		# s-boxes
		sbox_str = ""
		for j in range(0, 8):
			row = bin_to_dec(int(xor_right[j * 6] + xor_right[j * 6 + 5]))
			col = bin_to_dec(
				int(xor_right[j * 6 + 1] + xor_right[j * 6 + 2] +
					xor_right[j * 6 + 3] + xor_right[j * 6 + 4]))
			val = s_boxes[j][row][col]
			sbox_str = sbox_str + dec_to_bin(val)

		# permutation after sbox
		sbox_str = permute(sbox_str, permutation_after_sbox, 32)

		# XOR left and sbox_str
		result = xor(left, sbox_str)
		left = result

		if(i != 15):
			left, right = right, left

	combine = left + right

	# final permutation
	cipher_text = permute(combine, final_permutation, 64)
	return cipher_text


def generate_round_key(key, shift_table, compressing_key_arr):
	# Splitting
	left = key[0:28] # rkb for RoundKeys in binary
	right = key[28:56] # rk for RoundKeys in hexadecimal

	round_keys_arr = []


	for i in range(0, 16):
		# Shifting the bits by nth shifts by checking from shift table
		left = shift_left(left, shift_table[i])
		right = shift_left(right, shift_table[i])

		# Combination of left and right string
		combine_str = left + right

		# Compression of key from 56 to 48 bits
		round_key = permute(combine_str, compressing_key_arr, 48)

		round_keys_arr.append(round_key)
	return round_keys_arr