# noinspection SpellCheckingInspection
def main(args: list = None):
	"""Main Executor of jerryc05 module.

	:param args : The output from user
	"""
	import sys
	import jerryc05

	prt = print
	argv = sys.argv
	if args:
		args[:0] = argv
	else:
		args = argv
	__v = jerryc05.__version__
	# todo

	if len(args) < 2 or args[1] == '':
		prt(
			'No argument specified! I donno what to do, my flend!\n'
			'                                  .. .vr\n'
			'                                qBMBBBMBMY\n'
			'                               8BBBBBOBMBMv    叫你不给参数！\n'
			'                             iMBMM5vOY:BMBBv     不给参数！？\n'
			'             .r,             OBM;   .: rBBBBBY\n'
			'             vUL             7BB   .;7. LBMMBBM.\n'
			'            .@Wwz.           :uvir .i:.iLMOMOBM..\n'
			'             vv::r;             iY. ...rv,@arqiao.\n'
			'              Li. i:             v:.::::7vOBBMBL..\n'
			'              ,i7: vSUi,         :M7.:.,:u08OP. .\n'
			'                .N2k5u1ju7,..     BMGiiL7   ,i,i.\n'
			'                 :rLjFYjvjLY7r::.  ;v  vr... rE8q;.:,,\n'
			'                751jSLXPFu5uU@jerryc05.,1vjY2E89Yuzero.\n'
			'                BB:FMu rkM8Eq0PFjF15FZ0Xu15F25uuLuu25Gi.\n'
			'              ivSvvXL    :v58ZOGZXF2UUkFSFkU1u125uUJUUZ,\n'
			'            :@kevensun.      ,iY20GOXSUXkSuS2F5XXkUX5SEv.\n'
			'        .:i0BMBMBBOOBMUi;,        ,;8PkFP5NkPXkFqPEqqkZu.\n'
			'      .rqMqBBMOMMBMBBBM .           @kexianli.S11kFSU5q5\n'
			'    .7BBOi1L1MM8BBBOMBB..,          8kqS52XkkU1Uqkk1kUEJ\n'
			'    .;MBZ;iiMBMBMMOBBBu ,           1OkS1F1X5kPP112F51kU\n'
			'      .rPY  OMBMBBBMBB2 ,.          rME5SSSFk1XPqFNkSUPZ,.\n'
			'             ;;JuBML::r:.:.,,        SZPX0SXSP5kXGNP15UBr.\n'
			'                 L,    :@huhao.      :MNZqNXqSqXk2E0PSXPE .\n'
			'             viLBX.,,v8Bj. i:r7:,     2Zkqq0XXSNN0NOXXSXOU\n'
			'           :r2. rMBGBMGi .7Y, 1i::i   vO0PMNNSXXEqPYSecbone.\n'
			'           .i1r. .jkY,    vE. iY....  20Fq0q5X5F1S2F22uuv1M;'
		)

	elif args[1] == '-v':
		prt(__v)
	else:
		prt(f'Argument {args[1]} unsupported. Did you just mis-typed?')
	return


if __name__ == "__main__":
	main()
#     path = sys.path
#     path.insert(0, '.')
# main(['12306', 'beijing', 'fz', '20190505'])
