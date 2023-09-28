<h2><a href="https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/">2231. Largest Number After Digit Swaps by Parity</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">You are given a positive integer <code data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">num</code>. You may swap any two digits of <code data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">num</code> that have the same <strong data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">parity</strong> (i.e. both odd digits or both even digits).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">你得到一個正整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">num</code> 。您可以交換具有相同奇偶校驗的任意兩位數位 <code data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">num</code> （即兩個奇數或兩個偶數）。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">Return<em data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074"> the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">largest</strong> possible value of </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">num</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074"> after <strong data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">any</strong> number of swaps.</em><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回任意次數的交換 <code data-immersive-translate-effect="1" data-immersive_translate_walked="6392a0b2-def1-45c1-81d9-71dfc3914074">num</code> 后的最大可能值。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = 1234
<strong>Output:</strong> 3412
<strong>Explanation:</strong> Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = 65875
<strong>Output:</strong> 87655
<strong>Explanation:</strong> Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>
</div>