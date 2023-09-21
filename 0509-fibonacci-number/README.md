<h2><a href="https://leetcode.com/problems/fibonacci-number/">509. Fibonacci Number</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">The <b data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">Fibonacci numbers</b>, commonly denoted <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">F(n)</code> form a sequence, called the <b data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">0</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">1</code>. That is,<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">斐波那契數，通常表示 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">F(n)</code> 為形成一個序列，稱為斐波那契數列，使得每個數位都是前兩個數位的總和，從 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">0</code> 和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">1</code> 開始。那是</font></font></font></p>

<pre>F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">Given <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">n</code>, calculate <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">F(n)</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">n</code> ，計算 <code data-immersive-translate-effect="1" data-immersive_translate_walked="f04b617b-62d7-41ed-ab2c-72cbefe0e36b">F(n)</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>
</div>