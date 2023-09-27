<h2><a href="https://leetcode.com/problems/decoded-string-at-index/">880. Decoded String at Index</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">You are given an encoded string <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">s</code>. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得一個編碼字串 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">s</code> 。若要將字串解碼為磁帶，一次讀取一個字元的編碼字串，並執行以下步驟：</font></font></font></p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">If the character read is a letter, that letter is written onto the tape.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果讀出的字元是一封信，則該字母將寫在磁帶上。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">If the character read is a digit <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">d</code>, the entire current tape is repeatedly written <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">d - 1</code> more times in total.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果讀取的字元是數位 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">d</code> ，則整個當前磁帶總共重複寫入 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">d - 1</code> 更多次。</font></font></font></li>
</ul>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">Given an integer <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">k</code>, return <em data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">the </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">k<sup>th</sup></code><em data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962"> letter (<strong data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">1-indexed)</strong> in the decoded string</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">k</code> ，返回解碼字串中的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1725bdf6-6ec9-4739-822f-2299843f5962">k<sup>th</sup></code> 字母（1-索引）。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "leet2code3", k = 10
<strong>Output:</strong> "o"
<strong>Explanation:</strong> The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10<sup>th</sup> letter in the string is "o".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "ha22", k = 5
<strong>Output:</strong> "h"
<strong>Explanation:</strong> The decoded string is "hahahaha".
The 5<sup>th</sup> letter is "h".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "a2345678999999999999999", k = 1
<strong>Output:</strong> "a"
<strong>Explanation:</strong> The decoded string is "a" repeated 8301530446056247680 times.
The 1<sup>st</sup> letter is "a".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters and digits <code>2</code> through <code>9</code>.</li>
	<li><code>s</code> starts with a letter.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li>It is guaranteed that <code>k</code> is less than or equal to the length of the decoded string.</li>
	<li>The decoded string is guaranteed to have less than <code>2<sup>63</sup></code> letters.</li>
</ul>
</div>