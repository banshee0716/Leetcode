<h2><a href="https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/">2586. Count the Number of Vowel Strings in Range</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">You are given a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">0-indexed</strong> array of string <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">words</code> and two integers <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">left</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">right</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得一個字串 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">words</code> 和兩個整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">left</code> 和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">right</code> 0 索引陣列和 .</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">A string is called a <strong data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">vowel string</strong> if it starts with a vowel character and ends with a vowel character where vowel characters are <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'a'</code>, <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'e'</code>, <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'i'</code>, <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'o'</code>, and <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'u'</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果字串以元音字元開頭並以元音字元結尾，其中元音字元為 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'a'</code> 、 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'i'</code> 、 、 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'e'</code> 、 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'o'</code> 和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">'u'</code> ，則稱為元音字串。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">the number of vowel strings </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">words[i]</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110"> where </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">i</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110"> belongs to the inclusive range </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">[left, right]</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">i</code> 屬於包含範圍的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">[left, right]</code> 元音字串 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c010db77-3853-4e5d-ae3d-b226d9007110">words[i]</code> 的數量。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["are","amy","u"], left = 0, right = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
- "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
- "mu" is not a vowel string because it does not start with a vowel.
- "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
- "artro" is a vowel string because it starts with 'a' and ends with 'o'.
The number of vowel strings in the mentioned range is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li><code>0 &lt;= left &lt;= right &lt; words.length</code></li>
</ul>
</div>