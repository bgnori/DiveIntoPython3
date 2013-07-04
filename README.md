
Dive Into Python3 の章立てに沿った問題と問題への回答を検証するためのunittest

## 環境設定の仕方

python3.3をインストール済みであること.

次にsetup.shを用いて

    % ./setup.sh

とするとpackaging toolであるdistributeとpipがインストールされる.

次にpipを使って依存しているpackageを入れる

    % ./py3.3/bin/pip install -r freeze.txt

これでcheck.pyに必要なものがインストールされる。

## check.pyの使い方

    % python check.py exercises/chap2/q0002.py

とすると、標準出力にいろいろメッセージが出る.

前半は循環複雑度を測定した結果である.
課題の複雑さからすると5以上は好ましくない.

後半はpep8のチェックである(pep8.pyを使用)


## testの行い方

    % python -m tests.chap2.q0002

とすると、exercises/chap2/q0002.py がunittestされる.
結果が標準出力にでるので、全てokであること

testの実装が間違っていると思われる場合はissueをたててください.


Enjoy!


