

# What is Mizar? (And Why Is It So Cool?)

Imagine you're writing a super important essay. You'd probably use a spell checker to catch typos, right? Now, imagine you're a mathematician working on a massive, complex proof that's hundreds of pages long. A single tiny mistake, a small gap in logic, could bring the whole thing crashing down.

What if you had a "logic checker" for math?

That's exactly what **Mizar** is.

### The Ultimate Referee for Math

Think of Mizar as the strictest, smartest, most ruthless referee you've ever seen. [cite_start]It's a special computer program and language designed to do one thing incredibly well: check mathematical proofs for mistakes[cite: 2483].

Human mathematicians, even the most brilliant ones, can make mistakes. They might overlook a small step or assume something is true when it isn't. Mizar doesn't have that problem. It has no feelings and it never gets tired. It just checks the logic, step by step. If there's a flaw, it will find it.

This process is called **formal verification**. [cite_start]When a proof passes the Mizar checker, we can be extremely confident that it's 100% logically sound[cite: 755].

### How Does It Work?

It's a team effort between a special language, a giant library, and the checker itself.

1.  **The Mizar Language:** You can't just write a proof in normal English. You have to use the Mizar language, which is super precise. Every single statement has to be written in a way that the computer can understand without any confusion.

2.  **The Mizar Mathematical Library (MML):** This is the secret weapon. [cite_start]The MML is a massive, shared encyclopedia of mathematical knowledge that has already been checked and verified by Mizar[cite: 2485]. Think of it like a giant tech tree in a video game. [cite_start]You can't just invent a new theorem out of thin air; you have to build it using the definitions and theorems that are already unlocked in the library[cite: 2486].

3.  **The Proof Checker:** This is the referee program. When you're done writing your proof, you hand it to the checker. It reads every line and asks:
    * "Is this step a valid rule of logic?"
    * "Does this step use a fact that's already proven in the MML?"
    * "Is there any possible way this statement could be false?"

If the answer to any of these is no, the checker stops and points out the error. [cite_start]A common error is `*4: This inference is not accepted`, which is the computer's way of saying, "Nope, I don't see how you jumped from that step to this one. You need to explain it better!"[cite: 2601].

### Why Are We Using It?

In our project, we are building AIs that can reason and create new ideas. But how do we know if the AI is right? How do we make sure it's not just making plausible-sounding nonsense?

We use Mizar.

Our goal is to create a system where our AI can formulate a new mathematical idea and then automatically write a proof for it in the Mizar language. That proof is then handed to our Mizar verifier.

* If it **fails**, the AI knows it made a mistake, learns from the error, and tries again.
* [cite_start]If it **passes**, we have achieved something incredible: a piece of knowledge created by an AI that is **provably correct**[cite: 755].

By connecting our creative AI to a logical verifier like Mizar, we are building a system that doesn't just guess—it *knows*. That is the power of Mizar, and that is why it's a cornerstone of this project.
