<h2><a href="https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/">1894. Find the Student that Will Replace the Chalk<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">1894. 找到更換粉筆的學生</font></font></font></a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a" data-immersive-translate-paragraph="1">There are <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">n</code> students in a class numbered from <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0</code> to <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">n - 1</code>. The teacher will give each student a problem starting with the student number <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0</code>, then the student number <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">1</code>, and so on until the teacher reaches the student number <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">n - 1</code>. After that, the teacher will restart the process, starting with the student number <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0</code> again.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">一班有<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">n</code>學生，編號從<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0</code>到<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">n - 1</code> 。老師會給每個學生一個問題，從學號<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0</code>開始，然後是學號<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">1</code> ，以此類推，直到老師達到學號<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">n - 1</code> 。之後，老師將重新開始這個過程，再次從學號<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0</code>開始。</font></font></font></p>

<p data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a" data-immersive-translate-paragraph="1">You are given a <strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0-indexed</strong> integer array <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">chalk</code> and an integer <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">k</code>. There are initially <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">k</code> pieces of chalk. When the student number <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">i</code> is given a problem to solve, they will use <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">chalk[i]</code> pieces of chalk to solve that problem. However, if the current number of chalk pieces is <strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">strictly less</strong> than <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">chalk[i]</code>, then the student number <code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">i</code> will be asked to <strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">replace</strong> the chalk.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給你一個<strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">0 索引的</strong>整數陣列<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">chalk</code>和一個整數<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">k</code> 。最初有<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">k</code>支粉筆。當編號<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">i</code>學生需要解決一個問題時，他們將使用<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">chalk[i]</code>塊粉筆來解決這個問題。但是，如果當前粉筆塊的數量<strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">嚴格小於</strong><code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">chalk[i]</code> ，則將要求學號<code data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">i</code><strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">更換</strong>粉筆。</font></font></font></p>

<p data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">the <strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">index</strong> of the student that will <strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">replace</strong> the chalk pieces</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回將<em data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a"><strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">替換</strong>粉筆片的學生的<strong data-immersive-translate-walked="d5a1c58e-d5a3-4155-959d-3931086b7b1a">索引</strong></em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> chalk = [5,1,5], k = 22
<strong>Output:</strong> 0
<strong>Explanation: </strong>The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.
Student number 0 does not have enough chalk, so they will have to replace it.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> chalk = [3,4,1,2], k = 25
<strong>Output:</strong> 1
<strong>Explanation: </strong>The students go in turns as follows:
- Student number 0 uses 3 chalk so k = 22.
- Student number 1 uses 4 chalk so k = 18.
- Student number 2 uses 1 chalk so k = 17.
- Student number 3 uses 2 chalk so k = 15.
- Student number 0 uses 3 chalk so k = 12.
- Student number 1 uses 4 chalk so k = 8.
- Student number 2 uses 1 chalk so k = 7.
- Student number 3 uses 2 chalk so k = 5.
- Student number 0 uses 3 chalk so k = 2.
Student number 1 does not have enough chalk, so they will have to replace it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>chalk.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= chalk[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
</div>