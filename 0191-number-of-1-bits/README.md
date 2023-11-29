<h2><a href="https://leetcode.com/problems/number-of-1-bits/">191. Number of 1 Bits</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">Write a function that takes&nbsp;the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank" data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">Hamming weight</a>).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">編寫一個函數，該函數採用無符號整數的二進位表示形式，並返回它所具有的“1”位數（也稱為漢明權重）。</font></font></font></p>

<p><strong>Note:</strong></p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">請注意，在某些語言（如 Java）中，沒有無符號整數類型。在這種情況下，輸入將作為有符號整數類型給出。它應該不會影響您的實現，因為整數的內部二進位表示形式是相同的，無論是有符號還是無符號。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">In Java, the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank" data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">2's complement notation</a>. Therefore, in <strong class="example" data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">Example 3</strong>, the input represents the signed integer. <code data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">-3</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在 Java 中，編譯器使用 2 的補碼表示法表示有符號整數。因此，在示例 3 中，輸入表示有符號整數。 <code data-immersive-translate-effect="1" data-immersive_translate_walked="eeb10064-921b-4bef-ad1e-223880cc973f">-3</code> 。</font></font></font></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 00000000000000000000000000001011
<strong>Output:</strong> 3
<strong>Explanation:</strong> The input binary string <strong>00000000000000000000000000001011</strong> has a total of three '1' bits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 00000000000000000000000010000000
<strong>Output:</strong> 1
<strong>Explanation:</strong> The input binary string <strong>00000000000000000000000010000000</strong> has a total of one '1' bit.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> n = 11111111111111111111111111111101
<strong>Output:</strong> 31
<strong>Explanation:</strong> The input binary string <strong>11111111111111111111111111111101</strong> has a total of thirty one '1' bits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The input must be a <strong>binary string</strong> of length <code>32</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If this function is called many times, how would you optimize it?</div>