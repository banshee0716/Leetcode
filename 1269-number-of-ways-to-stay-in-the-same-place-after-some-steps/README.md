<h2><a href="https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/">1269. Number of Ways to Stay in the Same Place After Some Steps</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">You have a pointer at index <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">0</code> in an array of size <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">arrLen</code>. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在大小 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">arrLen</code> 的陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">0</code> 中，索引處有一個指標。在每一步中，您可以在陣列中向左移動 1 個位置，向右移動 1 個位置，或者停留在同一位置（指標任何時候都不應放置在數位外部）。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">Given two integers <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">steps</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">arrLen</code>, return the number of ways such that your pointer is still at index <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">0</code> after <strong data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">exactly</strong> <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">steps</code> steps. Since the answer may be too large, return it <strong data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">modulo</strong> <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">10<sup>9</sup> + 7</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定兩個整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">steps</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">arrLen</code> 和 ，返回方法的數量，使得指標在正好 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">steps</code> 的步驟之後仍然位於索引 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">0</code> 處。由於答案可能太大，因此將其返回模數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="b15645b1-1399-4fa8-b641-da409afaf378">10<sup>9</sup> + 7</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> steps = 3, arrLen = 2
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> steps = 2, arrLen = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> steps = 4, arrLen = 2
<strong>Output:</strong> 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= steps &lt;= 500</code></li>
	<li><code>1 &lt;= arrLen &lt;= 10<sup>6</sup></code></li>
</ul>
</div>