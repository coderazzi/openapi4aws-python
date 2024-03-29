Openapi 4 AWS
=============

-  Website: https://coderazzi.net/python/openapi4aws
-  Github: https://github.com/coderazzi/openapi4aws-python
-  Pypi: https://pypi.org/project/openapi4aws
-  License: MIT license

This is utility to enrich an openapi integration with information
specific for the AWS API Gateway. It allows defining route integrations
and authorizers to do automatic (re-)imports in API Gateway.

The openapi integration is extended on two parts: - security:
optionally, adding one or more authorizers. - paths: extending each
method with the associated authorizer and defining an endpoint.

The input to this utility is passed as parameters.

Security / Authorizers
----------------------

To specify an authorizer, use the following mandatory parameters:

-**authorizer.name**: name of the authorizer

-**authorizer.identity-source**: header containing the authorization,
like: $request.header.Authorization

-**authorizer.audience**: comma separated list of audiences for
this authorizer.

-**authorizer.issuer**

The following two parameters are currently optional:

-*authorizer.authorization-type* = **oauth2**: currently, it can be
only defined as “oauth2”.

-*authorizer.authorizer-type* = **jwt**:
currently, it can be only defined as “jwt”.

Multiple authorizers can be defined using a comma separated list in
**authorizer.name**, i.e.:

::

   authorizer.name=authorizer1, authorizer2

It is possible then to specify a different parameter for each authorizer
using the syntax:

-  **authorizer.audience.\ AUTHORIZER_NAME**\ =audience
-  **authorizer.issuer.\ AUTHORIZER_NAME**\ =issuer

Paths / Integrations
--------------------

To define routes, the syntax is:

-  **path.\ PATH**\ =full_uri[,authorizer_name,scopes]\*

For example:

::

   path.user.post=http://3.64.241.104:12121/user/post

This will define an endpoint for the route /user/post, using no
authorizers. Alternatively, authorizer plus scopes can be specified:

::

   path.user.post=http://3.64.241.104:12121/user/post,authorizer1,user.email,user.id

In this case, it uses the authorizer with name “authorizer1”, with
scopes “user.email” and “user.id”

Defining input / output
-----------------------

Three parameters manage the input / output tasks:

-**filename**: allows
to specify the input files to process, and it is possible to repeat this
parameter multiple times. It is an error if the designed filename does
not exist.

-**glob**: which supports specifying the input using
filename patterns. It is not an error if this pattern matches no names
in the file system.

-**output-folder**: optional, defines the output
folder. If not specified, the input files will be overwritten.

Defining the configuration in a separate file
---------------------------------------------

It is possible to specify any configuration parameters in a separate
file, using the argument:

::

   configuration=filename

This file should define the parameters in separate lines, using the same
syntax. Empty lines and starting with the character **#** are discarded.

It is possible to specify multiple external configuration files. An
example of a single file would be:

::

   # a comment
   authorizer.name=DubaixCognito,Other
   authorizer.identity-source=$request.header.Authorization
   authorizer.audience=2f0m9fcoiejij4316u574aq259,7ac34sujrb8gmvj2b6blpi7ruu
   authorizer.issuer=https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_1T9bfKHNp

   tag.Frontend=http://3.64.241.104:12121/tmp/,DubaixCognito,user.email,user.id
   path.user.scope2=http://OTHER_PATH:12122/path,Other,user.email
