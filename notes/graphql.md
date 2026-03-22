# GraphQL Testing

## Checks

- [ ] Identify GraphQL endpoints (`/graphql`, `/graphiql`, `/altair`, `/playground`, `/api/graphql`)
- [ ] Test for introspection (query the schema)
- [ ] Check for disabled introspection bypass (newline trick, GET vs POST)
- [ ] Enumerate types, queries, and mutations via introspection
- [ ] Test for authorization issues on queries and mutations
- [ ] Test query batching for brute force or rate limit bypass
- [ ] Test for excessive query depth/complexity (DoS)
- [ ] Check for information disclosure in error messages
- [ ] Test mutations for mass assignment / unauthorized data modification

## Basic Example

##### GraphQL Request

Code: graphql

```graphql
{
  users {
    id
    username
    role
  }
}
```

##### GraphQL Response

Code: graphql

```graphql
{
  "data": {
    "users": [
      {
        "id": 1,
        "username": "htb-stdnt",
        "role": "user"
      },
      {
        "id": 2,
        "username": "admin",
        "role": "admin"
      }
    ]
  }
}
```

## Introspection Queries

##### GraphQL Types

Code: graphql

```graphql
{
  __schema {
    types {
      name
    }
  }
}
```

##### GraphQL Queries

Code: graphql

```graphql
{
  __schema {
    queryType {
      fields {
        name
        description
      }
    }
  }
}
```

##### General Introspection

Code: graphql

```graphql
query IntrospectionQuery {
  __schema {
    queryType {
      name
    }
    mutationType {
      name
    }
    subscriptionType {
      name
    }
    types {
      ...FullType
    }
    directives {
      name
      description

      locations
      args {
        ...InputValue
      }
    }
  }
}

fragment FullType on __Type {
  kind
  name
  description

  fields(includeDeprecated: true) {
    name
    description
    args {
      ...InputValue
    }
    type {
      ...TypeRef
    }
    isDeprecated
    deprecationReason
  }
  inputFields {
    ...InputValue
  }
  interfaces {
    ...TypeRef
  }
  enumValues(includeDeprecated: true) {
    name
    description
    isDeprecated
    deprecationReason
  }
  possibleTypes {
    ...TypeRef
  }
}

fragment InputValue on __InputValue {
  name
  description
  type {
    ...TypeRef
  }
  defaultValue
}

fragment TypeRef on __Type {
  kind
  name
  ofType {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}
```

## Batching Example

Code: http

```http
POST /graphql HTTP/1.1
Host: 172.17.0.2
Content-Length: 86
Content-Type: application/json

[
	{
		"query":"{user(username: \"admin\") {uuid}}"
	},
	{
		"query":"{post(id: 1) {title}}"
	}
]
```

## Mutation Example

Code: graphql

```graphql
mutation {
  registerUser(
    input: {
      username: "vautia"
      password: "5f4dcc3b5aa765d61d8327deb882cf99"
      role: "user"
      msg: "newUser"
    }
  ) {
    user {
      username
      password
      msg
      role
    }
  }
}
```

## Tools

- [graphw00f](https://github.com/dolevf/graphw00f)
- [graphql-voyager](https://github.com/graphql-kit/graphql-voyager)
- [GraphQL-Cop](https://github.com/dolevf/graphql-cop)
- [InQL](https://github.com/doyensec/inql)

---

## References

- [PortSwigger - GraphQL API Vulnerabilities](https://portswigger.net/web-security/graphql)
- [PayloadsAllTheThings - GraphQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)
- [HackTricks - GraphQL](https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/graphql.html)
