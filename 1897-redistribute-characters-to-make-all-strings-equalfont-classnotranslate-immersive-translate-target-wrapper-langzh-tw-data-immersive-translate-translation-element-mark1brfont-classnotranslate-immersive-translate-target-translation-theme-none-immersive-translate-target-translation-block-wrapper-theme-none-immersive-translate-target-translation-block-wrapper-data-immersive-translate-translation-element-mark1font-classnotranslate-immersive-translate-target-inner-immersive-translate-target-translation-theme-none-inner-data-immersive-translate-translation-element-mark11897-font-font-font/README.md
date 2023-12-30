<h2><a href="https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/">1897. Redistribute Characters to Make All Strings Equal<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">1897. 重新分配字元以使所有字串相等</font></font></font></a></h2><h3>Easy</h3><hr><div><p>You are given an array of strings <code>words</code> (<strong>0-indexed</strong>).</p>

<p data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9" data-immersive-translate-paragraph="1">In one operation, pick two <strong data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">distinct</strong> indices <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">i</code> and <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">j</code>, where <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words[i]</code> is a non-empty string, and move <strong data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">any</strong> character from <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words[i]</code> to <strong data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">any</strong> position in <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words[j]</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在一個操作中，選取兩個不同的索引 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">i</code> 和 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">j</code> ，其中 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words[i]</code> 是非空字串，並將任何字元從 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words[i]</code> 移動到 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words[j]</code> 中的任意位置。</font></font></font></p>

<p data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9" data-immersive-translate-paragraph="1">Return <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">true</code> <em data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">if you can make<strong data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9"> every</strong> string in </em><code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words</code><em data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9"> <strong data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">equal </strong>using <strong data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">any</strong> number of operations</em>,<em data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9"> and </em><code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">false</code> <em data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">otherwise</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果可以使用任意數量的操作使每個字串 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">words</code> 相等， <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">false</code> 則返回，否則返回 <code data-immersive-translate-walked="2c997cbe-38f6-46db-991e-e428afed59f9">true</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["abc","aabc","bc"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Move the first 'a' in <code>words[1] to the front of words[2],
to make </code><code>words[1]</code> = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return <code>true</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["ab","a"]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make all the strings equal using the operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>
</div>