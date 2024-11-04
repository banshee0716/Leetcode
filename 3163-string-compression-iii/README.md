<h2><a href="https://leetcode.com/problems/string-compression-iii/">3163. String Compression III</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44" data-immersive-translate-paragraph="1">Given a string <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">word</code>, compress it using the following algorithm:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個字串<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">word</code> ，使用以下演算法對其進行壓縮：</font></font></font></p>

<ul>
	<li data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44" data-immersive-translate-paragraph="1">Begin with an empty string <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">comp</code>. While <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">word</code> is <strong data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">not</strong> empty, use the following operation:

	<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">以空字串<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">comp</code>開頭。當<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">word</code><strong data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">不為</strong>空時，請使用以下操作：</font></font></font><ul data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">
		<li data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44" data-immersive-translate-paragraph="1">Remove a maximum length prefix of <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">word</code> made of a <em data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">single character</em> <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">c</code> repeating <strong data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">at most</strong> 9 times.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">刪除由<em data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">單一字元</em><code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">c</code>組成的<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">word</code>的最大長度前綴，<strong data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">最多</strong>重複 9 次。</font></font></font></li>
		<li data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44" data-immersive-translate-paragraph="1">Append the length of the prefix followed by <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">c</code> to <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">comp</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">將<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">c</code>後面的前綴長度附加到<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">comp</code> 。</font></font></font></li>
	</ul>
	</li>
</ul>

<p data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44" data-immersive-translate-paragraph="1">Return the string <code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">comp</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回字串<code data-immersive-translate-walked="8872c976-289d-4373-8ed7-574f72d90f44">comp</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "abcde"</span></p>

<p><strong>Output:</strong> <span class="example-io">"1a1b1c1d1e"</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>comp = ""</code>. Apply the operation 5 times, choosing <code>"a"</code>, <code>"b"</code>, <code>"c"</code>, <code>"d"</code>, and <code>"e"</code> as the prefix in each operation.</p>

<p>For each prefix, append <code>"1"</code> followed by the character to <code>comp</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "aaaaaaaaaaaaaabb"</span></p>

<p><strong>Output:</strong> <span class="example-io">"9a5a2b"</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>comp = ""</code>. Apply the operation 3 times, choosing <code>"aaaaaaaaa"</code>, <code>"aaaaa"</code>, and <code>"bb"</code> as the prefix in each operation.</p>

<ul>
	<li>For prefix <code>"aaaaaaaaa"</code>, append <code>"9"</code> followed by <code>"a"</code> to <code>comp</code>.</li>
	<li>For prefix <code>"aaaaa"</code>, append <code>"5"</code> followed by <code>"a"</code> to <code>comp</code>.</li>
	<li>For prefix <code>"bb"</code>, append <code>"2"</code> followed by <code>"b"</code> to <code>comp</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>
</div>