<h2><a href="https://leetcode.com/problems/backspace-string-compare/">844. Backspace String Compare<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">844.退格字串比較</font></font></font></a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">Given two strings <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">s</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">t</code>, return <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">true</code> <em data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">if they are equal when both are typed into empty text editors</em>. <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">'#'</code> means a backspace character.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定兩個字串和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">t</code> ，如果它們相等，則返回，當 <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">true</code> 兩個字元串 <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">s</code> 都鍵入到空文本編輯器中時。 <code data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">'#'</code> 表示退格符。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="9077622b-1f82-41f9-9d5f-9a42d9e38f01">Note that after backspacing an empty text, the text will continue empty.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">請注意，在將空文本後退距後，文本將繼續為空。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "ab#c", t = "ad#c"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "ac".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "ab##", t = "c#d#"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "a#c", t = "b"
<strong>Output:</strong> false
<strong>Explanation:</strong> s becomes "c" while t becomes "b".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= s.length, t.length &lt;= 200</span></code></li>
	<li><span><code>s</code> and <code>t</code> only contain lowercase letters and <code>'#'</code> characters.</span></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it in <code>O(n)</code> time and <code>O(1)</code> space?</p>
</div>