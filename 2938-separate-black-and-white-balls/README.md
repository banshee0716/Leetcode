<h2><a href="https://leetcode.com/problems/separate-black-and-white-balls/">2938. Separate Black and White Balls</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277" data-immersive-translate-paragraph="1">There are <code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">n</code> balls on a table, each ball has a color black or white.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">桌上有<code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">n</code>球，每個球的顏色都是黑色或白色。</font></font></font></p>

<p data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277" data-immersive-translate-paragraph="1">You are given a <strong data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">0-indexed</strong> binary string <code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">s</code> of length <code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">n</code>, where <code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">1</code> and <code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">0</code> represent black and white balls, respectively.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個長度為<code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">n</code>的<strong data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">從 0 索引的</strong>二進位字串<code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">s</code> ，其中<code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">1</code>和<code data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">0</code>分別代表黑球和白球。</font></font></font></p>

<p data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277" data-immersive-translate-paragraph="1">In each step, you can choose two adjacent balls and swap them.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在每個步驟中，您可以選擇兩個相鄰的球並交換它們。</font></font></font></p>

<p data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">the <strong data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">minimum</strong> number of steps to group all the black balls to the right and all the white balls to the left</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">將所有黑球分組到右側並將所有白球分組到左側的<strong data-immersive-translate-walked="db6866ee-96a4-4c5a-bd1e-f9689795d277">最小</strong>步數</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "101"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "011".
Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "100"
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "010".
- Swap s[1] and s[2], s = "001".
It can be proven that the minimum number of steps needed is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "0111"
<strong>Output:</strong> 0
<strong>Explanation:</strong> All the black balls are already grouped to the right.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
</ul>
</div>