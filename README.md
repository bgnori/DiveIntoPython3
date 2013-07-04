Dive Into Python3 の章立てに沿った問題と問題への回答を検証するためのunittest

## 必要な物意する

#### githubでforkする

#### forkしたものを適当な場所にcloneする


## 環境設定の仕方

#### python3.3をインストール済みであること.

#### setup.shを用いて

    % ./setup.sh

とするとpyvenvで仮想環境が作られ、その環境の中に
packaging toolであるdistributeとpipがインストールされる.

#### 仮想環境を起動する

    % source py3.3/bin/activate

起動するとprompが変わる。

#### 仮想環境にpipを使って依存しているpackageを入れる

    (py3.3) % pip install -r freeze.txt

これでcheck.pyに必要なものがインストールされる。

#### 仮想環境を終了する

    (py3.3) % deactivate

## check.pyの使い方

    (py3.3) python check.py exercises/chap2/q0002.py

とすると、標準出力にいろいろメッセージが出る.

前半は循環複雑度を測定した結果である.
課題の複雑さからすると5以上は好ましくない.

後半はpep8のチェックである(pep8.pyを使用)


## testの行い方

    (py3.3) python -m tests.chap2.q0002

とすると、exercises/chap2/q0002.py がunittestされる.
結果が標準出力にでるので、全てokであること

testの実装が間違っていると思われる場合はissueをたててください.


Enjoy!
