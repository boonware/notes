# 14. Groups and Group Representations

## 14.1

Let $H_1$, $H_2$ be two subgroups of a group $G$. Show that $H_1 \cap H_2$ is also a subgroup.

### Solution

$$
    e \in H_1, e \in H_2 \implies e \in H_1 \cap H_2 \quad \text{(Identity)}
$$ 


$$
    \forall g \in H_1 \cap H_2 \implies g \in H_1, g \in H_2 \implies g^{-1} \in H_1, g^{-1} \in H_2 \implies g^{-1} \in H_1 \cap H_2 \quad \text{(Inverses)}
$$

$$
    \forall g, k \in H_1 \cap H_2 \implies g \in H_1, g \in H_2, k \in H_1, k \in H_2 \implies gk \in H_1, gk \in H_2 \implies gk \in H_1 \cap H_2 \quad \text{(Closure)}
$$

## 14.2 (a)
Let $G$ be any group.

The subset $Z(G)$ of $G$ consisting of those $g \in G$ that commute with all other elements of the group is called the _centre_ of the group. Show that $Z(G)$ is a subgroup of $G$.

### Solution

$$
    \forall g \in G, eg = ge \implies e \in Z(G) \quad \text{(Identity)}
$$

$$
    \exists g \in G \enspace | \enspace gk = kg \enspace \forall k \in G \implies g^{-1}gkg^{-1} = g^{-1}kgg^{-1} \iff kg^{-1} = g^{-1}k \iff g^{-1} \in Z(G) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G \enspace | \enspace gc = cg, kc = ck \enspace \forall c \in G \implies gkc = gck \iff gkc = cgk \iff gk \in Z(G) \quad \text{(Closure)}
$$

A similar approach shows that $kg \in Z(G)$, which is needed for closure.

## 14.2 (b)
If $g$ is an element of $G$, the set $C_G(g)$ of elements of $G$ that commute with $g$ is called the _centralizer_ of $g$ in $G$. Show that it is a subgroup of $G$.

### Solution

$$
    \forall g \in G, \enspace eg = ge \implies e \in C_G(g) \quad \text{(Identity)}
$$

$$
    \forall g \in C_G(g), \enspace gg^{-1} = g^{-1}g \iff g^{-1} \in C_G(g) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G \enspace | \enspace gk = kg \implies g(gk) = g(kg) \iff g(gk) = (gk)g \iff gk \in C_G(g) \quad \text{(Closure)}
$$

A similar approach shows that $kg \in C_G(g)$, which is needed for closure.

## 14.2 (c)
If $H$ is a subgroup of G, the set of elements of $G$ that commute with all elements of $H$ is the _centralizer_ $C_G(H)$ of $H$ in $G$. Show that it is a subgroup of $G$.

### Solution

$$
    \forall g \in H, \enspace eg = ge \implies e \in C_G(H) \quad \text{(Identity)}
$$

$$
    \forall g \in H, \enspace gg^{-1} = g^{-1}g \iff g^{-1} \in C_G(H), \enspace g \in C_G(H) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G, h \in H \enspace | \enspace gh = hg, \enspace kh = hk \implies kgh = khg \iff (kg)h = h(kg) \iff gk \in C_G(H) \quad \text{(Closure)}
$$

A similar approach shows that $kg \in C_G(H)$, which is needed for closure.

## 14.2 (d)
If $H$ is a subgroup of $G$, the set $N_G(H) \subset G$ consisting of those $g$ such that $g^{-1}Hg = H$ is called the _normalizer_ of $H$ in $G$. Show that $N_G(H)$ is a
subgroup of $G$, and that $H$ is a normal subgroup of $N_G(H)$.

### Solution (Part 1)

$$
    \forall h \in H, \enspace e^{-1}he \in H \implies e \in N_G(H) \quad \text{(Identity)}
$$

$$
    \exists g \in G \enspace | \enspace \forall h \in H, \enspace g^{-1}hg \in H \implies ggg^{-1}hgg^{-1}g^{-1} = ghg^{-1} \in H \iff g^{-1} \in N_G(H) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G \enspace | \enspace \forall h \in H, \enspace g^{-1}hg \in H, \enspace k^{-1}hk \in H \implies g^{-1}k^{-1}hkg \in H \iff (kg)^{-1}hkg \in H \iff kg \in N_G(H) \quad \text{(Closure)}
$$

A similar approach shows that $gk \in N_G(H)$, which is needed for closure.

### Solution (Part 2)
To show that $H$ is a normal subgroup of its normalizer $N_G(H)$, first show that $H$ is a _subset_ of $N_G(H)$. Due to closure, taking the product of every element of the _set_ $H$ with some specific element $h \in H$ just "reorders" the elements in the set, but doesn't change the set itself:

$$
    \forall h \in H, \enspace hH = Hh = H \implies h^{-1}Hh = H \implies H \subset N_G(H)
$$

Since $H$ is a subset of $N_G(H)$ and is also a group then it must be a subgroup. By definition of $N_G(H)$:

$$
    \forall m \in N_G(H), \forall h \in H, \enspace m^{-1}hm \in H \implies H \lhd N_G(H) 
$$

## 14.3
Show that the set of powers $g_0^n$ of an element $g_0 \in G$ form a subgroup. Now, let $p$ be a prime number. Recall that the set $\{1, 2, ..., p-1\}$ forms the group $(\mathbb{Z}_p)^{\times}$ under multiplication modulo $p$. By appealing to Langrange's Theorem, prove Fermat's Little Theorem.

### Solution (Part 1)

$$
    g_0^1 = g_0 \implies g_0^1 g_0^{-1} = g_0 g_0^{-1} \implies g_0^0 = e \quad \text{(Identity)}
$$

By definition, the inverse of any element is also a power and works as expected:

$$
    g_0^n g_0^{-n} = g_0^0 = e \quad \text{(Inverses)}
$$

The product of two powers $n$ and $k$ is a new element with power $n+k$. This property actually gives us both identity and inverses above:

$$
    g_0^n g_0^{k} = g_0^{n+k} \quad \text{(Closure)}
$$

### Solution (Part 2)

#### Fermat's Little Theorem

$$
    a^p = a \pmod p \quad a \in \mathbb{Z}, p \in \mathbb{P}
$$

Equivalently

$$
    a^p - a = np \quad n \in \mathbb{Z}
$$

If $a$ is coprime to $p$ then

$$
    a^{p-1} = 1 \pmod p
$$

Consider an element $g \in G$. The group $H = \{g^1, g^2, ... , g^n\}$ must either cycle through all elements of $G$ so that $H=G$ if $g$ is a generator, or form a subgroup $H \sub G$. If $g$ is a generator then $g^n = e$, that is, smaller powers of $g$ cannot be the identity, otherwise higher powers can never be reached:

$$
    g^{n-k} = e \implies g^{n-k}g = g \neq g^{n - k + 1}
$$

Since $n = |H|$ we have $g^{|H|} = e$. By Lagrange's Theorem we have $|G| = k|H|$ for  $k \in \mathbb{Z}$ so therefore

$$
    g^{|G|} = g^{k|H|} = (g^{|H|})^k = e^k = e
$$

Therefore, for  $\forall a \in (\mathbb{Z}_p)^{\times}$ where $|(\mathbb{Z}_p)^{\times}| = p - 1$, and since the powers of $a$ form a subgroup:

$$
    a^{(p-1)} = 1 \pmod p
$$

## 14.4
Use Fermat's Little Theorem to establish the identity underlying the algorithm for RSA public-key cryptography:

Let $n = pq$ for $p,q \in \mathbb{P}$. Using Euclid's algorithm for the highest common factor (HCF), also known as the Greatest Common Divisor (GCD), , firstly show that if $\exists k \in \mathbb{Z}$ such that $k$ is coprime to $(p-1)(q-1)$, then

$$
    \exists d \in \mathbb{Z} \enspace | \enspace dk = 1 \mod{(p-1)(q-1)}
$$

Then show that if 

$$
    C = M^k \mod{n} \quad \text{(Encryption)}
$$

then

$$
    M = C^d \mod{n} \quad \text{(Decryption)}
$$

(Note: $e$ is typically used to denote the encryption key, but $k$ is chosen here to avoid confusion with the identity element)

### Solution

For $a, b \in \mathbb{Z^+}$, $b \lt a$ and $gcd(a, b) = 1$, that is, they are coprime, we can define the _multiplicative group of integers modulo b_, $\mathbb{Z/nZ^{\times}}$. In our case, $gcd((p-1)(q-1), k)=1$ so therefore we have a group where multiplication is modulo $(p-1)(q-1)$. Since this forms a group, $d = k^{-1}$ must also be in the group such that

$$
    dk = 1 \mod{(p-1)(q-1)}
$$

Euler's Totient Function $\phi(m), m \in \mathbb{Z}$ is the number of integers less that $m$ that are coprime to $m$, where $p \in \mathbb{P} \iff \phi(p) = p-1$.

$$
    C^d \mod{n} = M^{dk} \mod n
$$

$$
    dk = 1 \mod \phi(n) \implies dk = u\phi(n) + 1, u \in \mathbb{Z}
$$

The Fermat–Euler Theorem for two coprime integers $a$ and $b$:

$$
    a^{\phi(a)} = 1 \mod{b}
$$

Therefore:

$$
    M^{dk} \mod{n} = (M^{u\phi(n)} \mod{n})(M \mod{n}) = M \mod{n}
$$
