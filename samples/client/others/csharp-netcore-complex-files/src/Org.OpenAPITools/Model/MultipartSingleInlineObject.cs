/*
 * MultipartFile test
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;
using OpenAPIClientUtils = Org.OpenAPITools.Client.ClientUtils;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// MultipartSingleInlineObject
    /// </summary>
    [DataContract(Name = "_multipart_single_inline_object")]
    public partial class MultipartSingleInlineObject : IEquatable<MultipartSingleInlineObject>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MultipartSingleInlineObject" /> class.
        /// </summary>
        /// <param name="file">One file.</param>
        public MultipartSingleInlineObject(System.IO.Stream file = default(System.IO.Stream))
        {
            this.File = file;
        }

        /// <summary>
        /// One file
        /// </summary>
        /// <value>One file</value>
        [DataMember(Name = "file", EmitDefaultValue = false)]
        public System.IO.Stream File { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class MultipartSingleInlineObject {\n");
            sb.Append("  File: ").Append(File).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return OpenAPIClientUtils.compareLogic.Compare(this, input as MultipartSingleInlineObject).AreEqual;
        }

        /// <summary>
        /// Returns true if MultipartSingleInlineObject instances are equal
        /// </summary>
        /// <param name="input">Instance of MultipartSingleInlineObject to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MultipartSingleInlineObject input)
        {
            return OpenAPIClientUtils.compareLogic.Compare(this, input).AreEqual;
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.File != null)
                {
                    hashCode = (hashCode * 59) + this.File.GetHashCode();
                }
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        public IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
